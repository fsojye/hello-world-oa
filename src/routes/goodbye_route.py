from typing import Annotated

from fastapi import APIRouter, FastAPI, HTTPException, Query

from models.serializers.base_response import BaseResponse
from models.serializers.goodbye import DelGoodbyeRequest
from services.planet_deleter_service import DeletePlanetException, PlanetDeleterService

router = APIRouter()


def include_router(app: FastAPI):
    app.include_router(router, prefix="/goodbye")


@router.delete(
    path="",
    response_model=BaseResponse,
    summary="Delete world",
)
async def say_goodbye(
    query_params: Annotated[DelGoodbyeRequest, Query()],
) -> BaseResponse:
    try:
        PlanetDeleterService().delete_planet(query_params.world)
        return BaseResponse(message=f"Goodbye world: {query_params.world}")
    except DeletePlanetException as e:
        raise HTTPException(status_code=500) from e
