from fastapi import FastAPI
from contextlib import asynccontextmanager
from tortoise import Tortoise
from app.api import ping, summaries
from app.db import init_db
import logging

logging.basicConfig(level=logging.DEBUG)

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # Initialize the database at startup
        init_db(app)
        yield  # Keeps the app running
    except Exception as e:
        logging.error(f"Error during startup: {e}")
        raise e
    finally:
        # Close database connections on shutdown
        await Tortoise.close_connections()

app = FastAPI(lifespan=lifespan)
app.include_router(ping.router)
app.include_router(summaries.router, prefix="/summaries", tags=["summaries"])