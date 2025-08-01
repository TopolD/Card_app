import asyncio

import pytest
import pytest_asyncio
from beanie import init_beanie
from httpx import ASGITransport, AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient

from app.card.models import ModelCard
from app.config import settings
from app.main import app as fastapi_app
from app.users.models import ModelUser


@pytest_asyncio.fixture(loop_scope="function", autouse=True)
async def db_client(event_loop):
    """
        create conn in database
    :param event_loop:
    :return:
    """
    client = AsyncIOMotorClient(settings.MONGODB_URI_TESTS)
    assert client

    await init_beanie(
        database=client[settings.MONGODB_DATABASE_TESTS],
        document_models=[ModelUser, ModelCard],
    )

    yield client

    await client.drop_database(settings.MONGODB_DATABASE_TESTS)

    client.close()


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(loop_scope="function")
async def ac():
    async with AsyncClient(
        transport=ASGITransport(app=fastapi_app), base_url="http://test"
    ) as ac:
        yield ac


@pytest_asyncio.fixture(loop_scope="function")
async def authenticated_ac():
    async with AsyncClient(
        transport=ASGITransport(app=fastapi_app), base_url="http://test"
    ) as ac:
        response = await ac.post(
            "/auth/login",
            json={
                "phone_number": "+380986419381",
                "password": "user",
            },
        )
        token = response.cookies.get("token")
        assert token

        ac.cookies.set("token", token)
        yield ac
