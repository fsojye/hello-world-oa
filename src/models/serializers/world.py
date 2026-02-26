from pydantic import BaseModel


class UpdateWorldRequest(BaseModel):
    name: str
    new_name: str


class DeleteWorldRequest(BaseModel):
    name: str


class GetWorldResponse(BaseModel):
    result: list
