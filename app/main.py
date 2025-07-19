from contextlib import asynccontextmanager


import uvicorn
from beanie import init_beanie
from fastapi import FastAPI
from pymongo import AsyncMongoClient
from pymongo.server_api import ServerApi

from app.card.models import   ModelCard
from app.config import settings
from app.users.router import router as router_users
from app.card.router import router as router_card

from app.users.models import ModelUser

@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncMongoClient(f"{settings.MONGODB_URL}.{settings.MONGODB_NAME}",server_api=ServerApi('1'))
    await init_beanie(
        database=client[f"{settings.MONGODB_NAME}"],
        document_models=[ModelUser,ModelCard]
    )
    try:
        yield
    finally:
        await client.close()


app = FastAPI(lifespan=lifespan)



app.include_router(router_users)
app.include_router(router_card)




if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080)
