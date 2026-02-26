from fastapi import HTTPException

from models.schemas.planet import Planet
from repositories.planet_repo import PlanetRepo


class PlanetUpdaterService:
    def __init__(self, planet_repo: PlanetRepo | None = None):
        self.planet_repo = planet_repo or PlanetRepo()

    def update_planet(self, name: str, new_name: str) -> Planet:
        try:
            planet = self.planet_repo.update_planet_name(name, new_name)
            if planet:
                return planet
        except Exception as e:
            raise UpdatePlanetException from e

        raise HTTPException(status_code=404)


class UpdatePlanetException(Exception):
    pass
