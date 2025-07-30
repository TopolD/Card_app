from datetime import date
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, constr
from pydantic_extra_types.payment import PaymentCardBrand, PaymentCardNumber

from app.card.models import Transaction


class CardSchema(BaseModel):
    name: str
    value: int
    history_transaction: list[Transaction] | None = None

    @property
    def brand(self) -> PaymentCardBrand:
        return self.number.brand

    @property
    def expired(self) -> bool:
        return self.exp < date.today()

    model_config = ConfigDict(from_attributes=True)
