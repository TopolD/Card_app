from httpx import AsyncClient
import pytest


# @pytest.mark.parametrize(
#     "name,email,password,status_code",
#     [
#         ('user1', "user1@user.com", 'user1', 200),
#         ('user2', "user2@user.com", 'user2', 200),
#         ('user3', "user3@user.com", 'user3', 200),
#         ('user1', "user1@user.com", 'user1', 408),
#
#     ]
# )
# async def test_register_user(name, email, password, status_code, ac: AsyncClient):
#     response = await ac.post('/auth/register', json={"name": name, "email": email, "password": password})
#
#     assert response.status_code == status_code
