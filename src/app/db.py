import os
from fastapi import FastAPI
from tortoise.contrib.fastapi import RegisterTortoise
from tortoise import Tortoise, run_async
import logging


# Configure logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

TORTOISE_ORM = {
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            "models": ["app.models.tortoise", "aerich.models"],
            "default_connection": "default",
        },
    },
}

def init_db(app: FastAPI) -> None:
    RegisterTortoise(
        app,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )

async def generate_schema() -> None:
    log.info("Initializing Tortoise...")

    await Tortoise.init(
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["models.tortoise"]},
    )
    log.info("Generating database schema via Tortoise...")
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


# new
if __name__ == "__main__":
    run_async(generate_schema())