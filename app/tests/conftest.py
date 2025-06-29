
import pytest

from app.config import settings
from app.database import engine
from app.main import app as fastapi_app
from httpx import AsyncClient,ASGITransport

@pytest.fixture(scope="function",autouse=True)
async def repare_database():

    assert settings.MODE =='TEST'
    collections = await engine.database.list_collection_names()

    assert collections

    for coll in collections:
        await engine.database.drop_collection(coll)

    for coll in collections:
        await engine.database.create_collection(coll)

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()



@pytest.fixture(scope="function")
async def ac() :
    async with AsyncClient(transport=ASGITransport(app=fastapi_app),base_url="http://test") as ac:
        yield ac