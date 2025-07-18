from typing import Annotated

from fastapi import APIRouter, Depends


from app.card.models import ModelCard, CardDao

from app.card.schemas import CardSchema
from app.exceptions import FailedToCreateMapException
from app.users.dependencies import get_current_user

from app.users.schemas import UserRead

router = APIRouter(
    prefix="/Card",
    tags=["Card"]
)

@router.get("")
async def get_card(user: Annotated[UserRead, Depends(get_current_user)]):
    card_obj = await CardDao.find_one_or_none({'user_id':user.id})

    return card_obj


@router.post("/add")
async def add_card(card:CardSchema,user: Annotated[UserRead, Depends(get_current_user)]):
    card_obj = await CardDao.add(ModelCard(
        name=card.name,
        value=card.value,
        history_transaction=card.history_transaction,
        user_id=user.id,
    ))
    if not card_obj:
        raise FailedToCreateMapException
    return card_obj



@router.delete("/del")
async def delete_card(user: Annotated[UserRead, Depends(get_current_user)]):
    card_obj = await CardDao.delete_item({"user_id":user.id})


