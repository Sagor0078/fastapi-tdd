import os
from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from app.config import get_settings, Settings
from tortoise.contrib.fastapi import RegisterTortoise
from tortoise import Tortoise

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    RegisterTortoise(
        app,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )
    yield  # Pause here while the app is running

    # Shutdown logic
    await Tortoise.close_connections()

app = FastAPI(lifespan=lifespan)

@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }