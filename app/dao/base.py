
from typing import Union
from bson import ObjectId


class BaseDao:
    model = None

    @classmethod
    async def add(cls, item):
        try:
            result = await cls.model.insert(item)
            return result
        except Exception as e:
            print(e)

    @classmethod
    async def find_all(cls, param):
        try:
            if param is None:
                return None
            result = cls.model.find(param)
            return result
        except Exception as e:
            print(e)

    @classmethod
    async def find_by_id(cls, id_: Union[str, ObjectId]):
        try:
            result = await cls.model.get(id_)
            return result
        except  Exception as e:
            print(e)

    @classmethod
    async def find_one_or_none(cls, param):
        try:
            if not param:
                return None
            result = await cls.model.find(param).first_or_none()
            return result
        except Exception as e:
            print(e)

    @classmethod
    async def delete_item(cls, item):
        try:
            await cls.model.delete(item)
            return None
        except Exception as e:
            print(e)
