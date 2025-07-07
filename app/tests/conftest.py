import asyncio

import pytest
from beanie import init_beanie
from pymongo import AsyncMongoClient

from app.config import settings

from app.main import app as fastapi_app

from httpx import AsyncClient, ASGITransport

from app.users.dao import ModelUser


@pytest.fixture()
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()



@pytest.fixture( autouse=True)
async def client(event_loop):
    client = AsyncMongoClient(settings.MONGODB_URI_TESTS)

    await init_beanie(
        database=client[settings.MONGODB_DATABASE_TESTS],
        document_models=[ModelUser]
    )


    yield client


    await client.close()


@pytest.fixture(scope="function")
async def ac():
    async with AsyncClient(transport=ASGITransport(app=fastapi_app), base_url="http://test") as ac:
        yield ac
