from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.models import Food
from app.utils.session import fetch_instance


async def validate_food(session: AsyncSession, instance_id: int) -> Food:
    food = await fetch_instance(session, model=Food, instance_id=instance_id)
    if not food:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Сущность с данным идентификатором отсутствует",
        )
    return food
