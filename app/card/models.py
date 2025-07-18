from typing import Optional

from beanie import Document, Link

from app.card.schemas import CardSchema
from app.dao.base import BaseDao
from app.users.models import ModelUser




class ModelCard(Document):
    name: str
    value: Optional[int] = None
    history_transaction: Optional[list[dict]] = None
    user_id: Link[ModelUser]

    class Settings:
        name = "Cards"


class CardDao(BaseDao):
    model = ModelCard


