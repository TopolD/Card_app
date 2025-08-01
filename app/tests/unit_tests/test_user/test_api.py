import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "name,phone_number,password,status_code",
    [
        ("user", "+380986419381", "user", 200),
    ],
)
async def test_register_user(
    name, phone_number, password, status_code, ac: AsyncClient
):
    response = await ac.post(
        "/auth/register",
        json={"name": name, "phone_number": phone_number, "password": password},
    )

    assert response.status_code == status_code


@pytest.mark.parametrize(
    "name,phone_number,password,status_code",
    [
        ("user", "+380986419381", "user", 200),
    ],
)
async def test_login_user(name, phone_number, password, status_code, ac: AsyncClient):
    new_user = await ac.post(
        "/auth/register",
        json={"name": name, "phone_number": phone_number, "password": password},
    )

    assert new_user.status_code == status_code

    response = await ac.post(
        "/auth/login",
        json={"name": name, "phone_number": phone_number, "password": password},
    )
    assert response.status_code == status_code
