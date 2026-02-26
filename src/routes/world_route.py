from fastapi import APIRouter, FastAPI, HTTPException

from models.serializers.base_response import BaseResponse
from models.serializers.world import (
    GetWorldResponse,
    UpdateWorldRequest,
)
from services.planet_fetcher_service import PlanetFetcherService
from services.planet_updater_service import PlanetUpdaterService, UpdatePlanetException

router = APIRouter()


def include_router(app: FastAPI):
    app.include_router(router, prefix="/worlds")


@router.get(
    path="",
    response_model=GetWorldResponse,
    summary="Get all worlds",
)
async def get_worlds() -> GetWorldResponse:
    service = PlanetFetcherService()
    worlds = service.get_planets()
    return GetWorldResponse(result=[world.name for world in worlds])


@router.put(
    path="",
    response_model=BaseResponse,
    summary="Update a world",
)
async def update_world(request: UpdateWorldRequest) -> BaseResponse:
    try:
        world = PlanetUpdaterService().update_planet(request.name, request.new_name)
        return BaseResponse(
            message=(
                f"{request.name}, born on {world.date_created}, "
                f"from {world.date_modified} you shall be known as {request.new_name}"
            )
        )
    except UpdatePlanetException as e:
        raise HTTPException(500) from e
