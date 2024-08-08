from typing import Optional, Sequence

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.core.context import ApplicationContext
from app.models import FoodCategory, Topping
from app.models.food import Food
from app.schemas.food.create_food import CreateFoodSchema
from app.schemas.food.patch_food import PatchFoodSchema
from app.schemas.food.update_food import UpdateFoodSchema
from app.utils.decorators.handle_request import handle_request
from app.utils.session import fetch_instance, update_instance_fields
from app.validation.validate_food import validate_food


class FoodService:

    @handle_request
    async def get_food(self, context: ApplicationContext, id: int) -> Food:
        return await fetch_instance(context.session, model=Food, instance_id=id)

    @handle_request
    async def get_foods(
        self,
        context: ApplicationContext,
        is_vegan: Optional[bool] = None,
        is_special: Optional[bool] = None,
    ) -> Sequence[Food]:
        stmt = (
            select(FoodCategory)
            .join(Food, Food.category_id == FoodCategory.id)
            .group_by(FoodCategory.id)
        )
        if is_vegan is not None:
            stmt = stmt.where(Food.is_vegan.is_(is_vegan))
        if is_special is not None:
            stmt = stmt.where(Food.is_special.is_(is_special))
        stmt = stmt.order_by(FoodCategory.id)
        return (await context.session.execute(stmt)).scalars().fetchall()

    @handle_request
    async def create_food(
        self, context: ApplicationContext, data: CreateFoodSchema
    ) -> Food:
        food = Food(**data.model_dump())
        context.session.add(food)
        await context.session.flush()
        return food

    @handle_request
    async def update_food(
        self, context: ApplicationContext, data: UpdateFoodSchema, id: int
    ) -> Food:
        food = await validate_food(context.session, instance_id=id)
        update_instance_fields(food, new_fields=data.model_dump())
        return food

    @handle_request
    async def patch_food(
        self, context: ApplicationContext, data: PatchFoodSchema, id: int
    ) -> Food:
        food = await validate_food(context.session, instance_id=id)
        if data.name is not None:
            food.name = data.name
        if data.description is not None:
            food.description = data.description
        if data.price is not None:
            food.price = data.price
        if data.is_special is not None:
            food.is_special = data.is_special
        if data.is_vegan is not None:
            food.is_vegan = data.is_vegan
        if data.is_publish is not None:
            food.is_publish = data.is_publish
        if data.category_id is not None:
            food.category_id = data.category_id
        return food
