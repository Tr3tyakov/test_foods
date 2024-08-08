from typing import Optional

from app.schemas.base.base import BaseSchema


class PatchFoodSchema(BaseSchema):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None
    is_special: Optional[bool] = None
    is_vegan: Optional[bool] = None
    is_publish: Optional[bool] = None
    category_id: Optional[int] = None
