import time
from contextlib import asynccontextmanager

import uvicorn
from beanie import init_beanie
from fastapi import FastAPI, Request
from pymongo import AsyncMongoClient
from pymongo.errors import PyMongoError
from pymongo.server_api import ServerApi
from starlette.middleware.sessions import SessionMiddleware

from app.card.models import ModelCard
from app.card.router import router as router_card
from app.config import settings
from app.logger import log
from app.users.models import ModelUser
from app.users.router import router as router_users


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        client = AsyncMongoClient(
            f"{settings.MONGODB_URL}.{settings.MONGODB_NAME}", server_api=ServerApi("1")
        )
        await init_beanie(
            database=client[f"{settings.MONGODB_NAME}"],
            document_models=[ModelUser, ModelCard],
        )
        try:
            yield
        finally:
            await client.close()
    except PyMongoError:
        log.error("PyMongo error", exc_info=True)


app = FastAPI(lifespan=lifespan)


app.add_middleware(SessionMiddleware, secret_key=f"{settings.SECRET_KEY}")
app.include_router(router_users)
app.include_router(router_card)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    log.info("Request execute time: %s", extra={"process_time": round(process_time, 3)})
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080)
