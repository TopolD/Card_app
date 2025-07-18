from datetime import date


from pydantic import BaseModel, ConfigDict, constr
from pydantic_extra_types.payment import PaymentCardBrand, PaymentCardNumber

class CardSchema(BaseModel):
    name: str
    value:int
    history_transaction:list[dict]

    @property
    def brand(self) -> PaymentCardBrand:
        return self.number.brand

    @property
    def expired(self) -> bool:
        return self.exp < date.today()

    model_config = ConfigDict(from_attributes=True)