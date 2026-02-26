from pydantic import BaseModel


class DelGoodbyeRequest(BaseModel):
    world: str
