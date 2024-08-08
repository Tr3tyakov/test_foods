from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.models.base.base import BaseModel
from app.models.references.topping_food_references import ToppingFoodReference


class Food(BaseModel):
    """Блюдо"""

    id = Column(
        Integer, primary_key=True, autoincrement=True, comment="Идентификатор блюда"
    )
    name = Column(String, comment="Наименование блюда")
    description = Column(Text, comment="Описание блюда")
    price = Column(Integer, comment="Стоимость блюда")
    is_special = Column(Boolean, comment="Особенность блюда")
    is_vegan = Column(Boolean, comment="Веганское блюдо")
    is_publish = Column(Boolean, comment="Опубликованность блюда")
    category_id = Column(
        Integer, ForeignKey("food_category.id"), comment="Идентификатор категории блюда"
    )
    toppings = relationship(
        "Topping",
        secondary=ToppingFoodReference.__tablename__,
        lazy="subquery",
        order_by="Topping.id",
    )
