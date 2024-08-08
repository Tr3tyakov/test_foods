from sqlalchemy import Column, Integer, String

from app.models.base.base import BaseModel


class Topping(BaseModel):
    """Ингредиент"""

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        comment="Идентификатор ингредиента",
    )
    name = Column(String, comment="Наименование ингредиента")
