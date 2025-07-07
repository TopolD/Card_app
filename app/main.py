from contextlib import asynccontextmanager

import uvicorn
from beanie import init_beanie
from fastapi import FastAPI
from pymongo import AsyncMongoClient
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.config import settings
from app.users.router import router as router_users
from app.users.dao import ModelUser

@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncMongoClient(settings.MONGODB_URI)

    await init_beanie(
        database=client[f"{settings.MONGODB_DATABASE}"],
        document_models=[ModelUser]
    )
    try:
        yield
    finally:
        await client.close()


app = FastAPI(lifespan=lifespan)

app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

app.include_router(router_users)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080)
