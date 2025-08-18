import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "name,value,history_transaction,status_code", [("testcard", 100, [], 200)]
)
async def test_add_card_user(
    name, value, history_transaction, status_code, authenticated_ac: AsyncClient
):
    response = await authenticated_ac.post(
        "/Card/add",
        json={"name": name, "value": value, "history_transaction": history_transaction},
    )
    assert response.status_code == status_code
