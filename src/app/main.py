from fastapi import FastAPI
from contextlib import asynccontextmanager
from tortoise import Tortoise
from app.api import ping, summaries
from app.db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize the database at startup
    init_db(app)
    yield  # Keeps the app running

    # Close database connections on shutdown
    await Tortoise.close_connections()

app = FastAPI(lifespan=lifespan)
app.include_router(ping.router)
app.include_router(summaries.router, prefix="/summaries", tags=["summaries"])  

