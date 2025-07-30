from datetime import date
from typing import Optional

from beanie import Document, Link
from pydantic import BaseModel

from app.dao.base import BaseDao
from app.users.models import ModelUser


class Transaction(BaseModel):
    name: str
    value: int
    date: date


class ModelCard(Document):
    name: str
    value: int | None = None
    history_transaction: Transaction | None = None
    user_id: Link[ModelUser]

    class Settings:
        name = "Cards"


class CardDao(BaseDao):
    model = ModelCard
