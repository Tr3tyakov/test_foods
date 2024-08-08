from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.models.base.base import BaseModel


class FoodCategory(BaseModel):
    """Категория блюда"""

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        comment="Идентификатор категории блюда",
    )
    name = Column(String, comment="Наименование категории")
    is_publish = Column(Boolean, default=False, comment="Опубликованность категории")
