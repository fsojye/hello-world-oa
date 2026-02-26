from models.schemas.planet import Planet
from repositories.planet_repo import PlanetRepo


class PlanetCreatorService:
    def __init__(self, planet_repo: PlanetRepo | None = None):
        self.planet_repo = planet_repo or PlanetRepo()

    def create_planet(self, name: str) -> Planet:
        try:
            return self.planet_repo.create_planet(name)
        except Exception as e:
            raise CreatePlanetException from e


class CreatePlanetException(Exception):
    pass
