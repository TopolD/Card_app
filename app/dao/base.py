from app.database import engine


class BaseDao:
    model = None

    @classmethod
    async def add_item(cls, item):
        try:

            result = await engine.save(item)
            return result
        except Exception as e:
            print(e)
    @classmethod
    async def find_all(cls, param):
        try:
            if param is None:
                return None
            result = await engine.find(cls.model, param)
            return result
        except Exception as e:
            print(e)

    @classmethod
    async def find_by_id(cls, id: int):
        try:
            result = await engine.find_one(cls.model, cls.model.id == id)
            return result
        except  Exception as e:
            print(e)

    @classmethod
    async def find_one_or_none(cls, param):
        try:
            if not param:
                return None
            return await engine.find_one(cls.model, param)
        except Exception as e:
            print(e)

    @classmethod
    async def delete_item(cls, item):
        try:
            await engine.delete(item)
            return None
        except Exception as e:
            print(e)
