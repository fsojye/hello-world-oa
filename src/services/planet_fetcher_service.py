from fastapi import HTTPException

from models.schemas.planet import Planet
from repositories.planet_repo import PlanetRepo


class PlanetFetcherService:
    def __init__(self, planet_repo: PlanetRepo | None = None):
        self.planet_repo = planet_repo or PlanetRepo()

    def get_planet_by_name(self, name: str) -> Planet:
        try:
            planet = self.planet_repo.get_by_planet_name(name)
            if planet:
                return planet
        except Exception as e:
            raise GetPlanetByNameException from e

        raise HTTPException(status_code=404)

    def get_planets(self) -> list[Planet]:
        return self.planet_repo.get_all()


class GetPlanetByNameException(Exception):
    pass
