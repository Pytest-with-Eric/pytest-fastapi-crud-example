from datetime import datetime
from typing import List
from pydantic import BaseModel, Field


class UserBaseSchema(BaseModel):
    id: str | None = None
    first_name: str = Field(
        ..., description="The first name of the user", example="John"
    )
    last_name: str = Field(..., description="The last name of the user", example="Doe")
    address: str | None = None
    activated: bool = False
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListUserResponse(BaseModel):
    status: str
    results: int
    users: List[UserBaseSchema]
