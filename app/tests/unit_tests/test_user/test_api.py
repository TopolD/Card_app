import pytest_asyncio
from httpx import AsyncClient
import pytest


@pytest.mark.parametrize(
    "name,phone_number,password,status_code",
    [
        ('user',"+380986419381", 'user', 200),
        ('user2',"+380937654321", 'user2', 200),
        ('user3',"+380671234567",'user3', 200),
        ('user',"+380986419381", 'user', 409),

    ]
)
async def test_register_user(name, phone_number,password, status_code, ac: AsyncClient):
    response = await ac.post('/auth/register', json={
        "name": name,"phone_number":phone_number, "password": password
    })

    assert response.status_code == status_code


@pytest.mark.parametrize(
    "name,phone_number,password,status_code",
    [
        ("user","+380986419381", 'user', 200),
        ("user1","+380671234567", '6YH5TJOIEAGRO[IJETGROIJMHERT', 401),
    ]
)
async def test_login_user(name,phone_number, password, status_code, ac: AsyncClient):
    response = await ac.post('/auth/login', json={"name":name,"phone_number":phone_number, "password": password})
    assert response.status_code == status_code