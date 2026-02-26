from pydantic import BaseModel


class PostHelloPayload(BaseModel):
    world: str
