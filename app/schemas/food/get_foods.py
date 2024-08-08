from typing import List

from app.schemas.base.base import BaseSchema


class ResponseToppingSchema(BaseSchema):
    name: str


class ResponseFoodSchema(BaseSchema):
    name: str
    description: str
    price: int
    is_vegan: bool
    is_special: bool
    toppings: List[ResponseToppingSchema]

    def model_post_init(self, __context):
        self.toppings = [topping.name for topping in self.toppings if self.toppings]


class ResponseCategorySchema(BaseSchema):
    id: int
    name: str
    foods: List[ResponseFoodSchema] = []
