from sqlalchemy import Column, ForeignKey, Integer

from app.models.base.base import BaseModel


class ToppingFoodReference(BaseModel):
    """Таблица m2m для связи ингредиентов и блюд"""

    food_id = Column(
        Integer,
        ForeignKey("food.id", ondelete="CASCADE"),
        primary_key=True,
        comment="Идентификатор блюда",
    )
    topping_id = Column(
        Integer,
        ForeignKey("topping.id", ondelete="CASCADE"),
        primary_key=True,
        comment="Идентификатор ингредиента",
    )
