from typing import Optional

from app.schemas.base.base import BaseSchema


class CreateFoodSchema(BaseSchema):
    name: str
    description: str
    price: int
    is_special: bool
    is_vegan: bool
    is_publish: bool
    category_id: Optional[int] = None
