from fastapi import APIRouter, FastAPI, HTTPException

from models.serializers.base_response import BaseResponse
from models.serializers.hello import PostHelloPayload
from services.planet_creator_service import CreatePlanetException, PlanetCreatorService

router = APIRouter()


def include_router(app: FastAPI):
    app.include_router(router, prefix="/hello")


@router.post(
    path="",
    response_model=BaseResponse,
    summary="Create world",
)
async def create_world(payload: PostHelloPayload) -> BaseResponse:
    try:
        planet_fetcher_service = PlanetCreatorService()
        planet = planet_fetcher_service.create_planet(payload.world)
        return BaseResponse(message=f"Hello, planet {planet.id} aka {planet.name}")
    except CreatePlanetException as e:
        raise HTTPException(status_code=500) from e
