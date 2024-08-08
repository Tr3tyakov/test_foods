from typing import List, Optional

from fastapi import APIRouter, Depends, Query, Request

from app.schemas.food.base_food import ResponseFoodSchema
from app.schemas.food.create_food import CreateFoodSchema
from app.schemas.food.get_foods import ResponseCategorySchema
from app.schemas.food.patch_food import PatchFoodSchema
from app.schemas.food.update_food import UpdateFoodSchema
from app.services.food_service import FoodService

router = APIRouter(tags=["food"], prefix="/food")


@router.get(
    "/",
    description="Получение списка блюд",
    response_model=List[ResponseCategorySchema],
)
async def get_foods(
        request: Request,
        service: FoodService = Depends(),
        is_vegan: Optional[bool] = Query(False, description="Веганское блюдо"),
        is_special: Optional[bool] = Query(False, description="Особенность блюда"),
):
    return await service.get_foods(request, is_vegan=is_vegan, is_special=is_special)


@router.get("/{id}", description="Получение конкретного блюда")
async def get_food(
        request: Request, id: int, service: FoodService = Depends()
) -> ResponseFoodSchema:
    return await service.get_food(request, id=id)


@router.post("/", description="Создание блюда")
async def create_food(
        request: Request, data: CreateFoodSchema, service: FoodService = Depends()
):
    return await service.create_food(request, data=data)


@router.put("/{id}", description="Обновление блюда")
async def update_food(
        request: Request, data: UpdateFoodSchema, id: int, service: FoodService = Depends()
) -> ResponseFoodSchema:
    return await service.update_food(request, data, id=id)


@router.patch("/{id}", description="Обновление блюда")
async def patch_food(
        request: Request, id: int, data: PatchFoodSchema, service: FoodService = Depends()
) -> ResponseFoodSchema:
    return await service.patch_food(request, data, id=id)
