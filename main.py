import asyncio
import os

from fastapi import FastAPI

from alembic import command
from alembic.config import Config

from src.api import contacts, utils

app = FastAPI()

app.include_router(contacts.router, prefix="/api")
app.include_router(utils.router, prefix="/api")


async def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


async def lifespan(app: FastAPI):
    await run_migrations()
    yield
    print("👋 Shutting down...")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
