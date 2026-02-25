from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session

from src.models.schemas.planet import Planet


class Database:
    def __init__(self):
        engine = create_engine('sqlite:///helloworld.db')
        self.sesion_factory = scoped_session(
            sessionmaker(expire_on_commit=False, autocommit=False, autoflush=False, bind=engine)
        )
        
    @contextmanager
    def session(self) -> Generator[Session, None, None]:
        session = self.sesion_factory()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()


class PlanetRepo(Database):
    def get_by_planet_name(self, name: str) -> Planet | None:
        with self.session() as session:
            return (
                session.query(Planet)
                .filter(Planet.name == name)
                .one_or_none()
            )
    
    def get_all(self) -> list[Planet]:
        with self.session() as session:
            return session.query(Planet).all()
    
    def update_planet_name(self, name: str, new_name: str) -> Planet | None:
        with self.session() as session:
            planet = session.query(Planet).filter(Planet.name == name).one_or_none()
            if planet:
                planet.name = new_name
                session.commit()
                session.refresh(planet)
            return planet
    
    def delete_planet_by_name(self, name: str) -> bool:
        with self.session() as session:
            planet = session.query(Planet).filter(Planet.name == name).one_or_none()
            if planet:
                session.delete(planet)
                session.commit()
                return True
            return False
    
    def create_planet(self, name: str) -> Planet:
        with self.session() as session:
            planet = Planet(name=name)
            session.add(planet)
            session.commit()
            session.refresh(planet)
            return planet