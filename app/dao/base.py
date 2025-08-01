from bson import ObjectId
from pydantic import ValidationError
from pymongo.errors import PyMongoError

from app.exceptions import ExceptionDatabase


class BaseDao:
    model = None

    @classmethod
    async def add(cls, item):
        """
            add an item to the database
        :param item:
        :return:result
        """

        try:
            result = await cls.model.insert(item)
            return result
        except (ValidationError, PyMongoError) as e:
            await ExceptionDatabase(e, name="add")

    @classmethod
    async def find_all(cls, param):
        try:
            if param is None:
                return None
            result = cls.model.find(param)
            return result
        except (ValidationError, PyMongoError) as e:
            await ExceptionDatabase(e, name="find_all")

    @classmethod
    async def find_by_id(cls, id_: str | ObjectId):
        try:
            if id_ is None:
                return None
            result = await cls.model.get(id_)
            return result
        except (ValidationError, PyMongoError) as e:
            await ExceptionDatabase(e, name="find_by_id")

    @classmethod
    async def find_one_or_none(cls, param):
        try:
            if not param:
                return None
            result = await cls.model.find(param).first_or_none()
            return result
        except (ValidationError, PyMongoError) as e:
            await ExceptionDatabase(e, name="find_one_or_none")

    @classmethod
    async def delete_item(cls, item):
        try:
            await cls.model.delete(item)
            return None
        except (ValidationError, PyMongoError) as e:
            await ExceptionDatabase(e, name="delete_item")
