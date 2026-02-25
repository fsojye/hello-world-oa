from fastapi import HTTPException

from repositories.planet_repo import PlanetRepo


class PlanetDeleterService:
    def __init__(self, planet_repo: PlanetRepo | None = None):
        self.planet_repo = planet_repo or PlanetRepo()

    def delete_planet(self, name: str) -> bool:
        try:
            is_deleted = self.planet_repo.delete_planet_by_name(name)
            if is_deleted:
                return is_deleted
        except Exception as e:
            raise DeletePlanetException(e)
        
        raise HTTPException(status_code=404)


class DeletePlanetException(Exception):
    pass