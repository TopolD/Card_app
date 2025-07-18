from app.users.models import UsersDao, ModelUser


async def test_add_item(db_client):
    new_user = await UsersDao.add(ModelUser(
        name='user',
        email='tests@tests.com',
        password='1234'
    ))
    assert new_user.name == 'user'

    new_user = await UsersDao.find_by_id(
        new_user.id
    )

    assert new_user.name == 'user'

    new_request = await UsersDao.find_one_or_none({'name': new_user.name})


    assert new_request.name == 'user'

    new_request = await UsersDao.find_all({'name': new_user.name})

    assert new_request is not None
