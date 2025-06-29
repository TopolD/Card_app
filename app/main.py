
from contextlib import asynccontextmanager
from logging import info

import uvicorn
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from app.config import settings
from app.users.router import router as router_users

@asynccontextmanager
async def db_lifespan(app: FastAPI):
    if settings.MODE == 'TEST':
        app.mongodb_client = AsyncIOMotorClient(settings.MONGODB_URI_TESTS)
    else:
        app.mongodb_client = AsyncIOMotorClient(settings.MONGODB_URI)
    app.database = app.mongodb_client.get_default_database()
    ping_response = await app.mongodb_client.admin.command("ping")
    if int(ping_response["ok"]) != 1:
        raise Exception("Problem connecting to database cluster.")
    else:
        info("Connected to database cluster.")

    yield
    app.mongodb_client.close()

app = FastAPI(lifespan=db_lifespan)

app.include_router(router_users)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080)