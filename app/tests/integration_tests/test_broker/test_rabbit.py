import pytest
from faststream.rabbit import TestRabbitBroker, fastapi

router = fastapi.RabbitRouter()


@router.subscriber("test")
async def handler(msg: str): ...


@pytest.mark.asyncio
async def test_router():
    async with TestRabbitBroker(router.broker) as br:
        await br.publish("Hi", queue="test")

        handler.mock.assert_called_once_with("Hi")
