from httpx import AsyncClient
import pytest


# @pytest.mark.parametrize(
#     "name,email,password,status_code",
#     [
#         ('user', "user@user.com", 'user', 200),
#         ('user2', "user2@user.com", 'user2', 200),
#         ('user3', "user3@user.com", 'user3', 200),
#         ('user', "user@user.com", 'user', 409),
#
#     ]
# )
# async def test_register_user(name, email, password, status_code, ac: AsyncClient):
#     response = await ac.post('/auth/register', json={"name": name, "email": email, "password": password})
#
#     assert response.status_code == status_code



@pytest.mark.parametrize(
    "name,email,password,status_code",
    [
        ("user","user@user.com", 'user', 200),
        ("user1","user@user.com", '6YH5TJOIEAGRO[IJETGROIJMHERT', 401),
    ]
)
async def test_login_user(name,email, password, status_code, ac: AsyncClient):
    response = await ac.post('/auth/login', json={"name":name,"email": email, "password": password})
    assert response.status_code == status_code