import uuid
from typing import Optional
from pydantic import BaseModel, Field

class PlayerModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    image_url: str = Field(...)
    current_team: str = Field(...)
    birth_year: int = Field(..., le=2023)
    preferred_foot: str = Field(...)
    height: int = Field(..., le=250)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "Lionel Messi",
                "image_url": "https://example.com/messi.jpg",
                "current_team": "Inter Miami CF",
                "birth_year": 1987,
                "preferred_foot": "Left",
                "height": 170
            }
        }

class UpdatePlayerModel(BaseModel):
    name: Optional[str]
    image_url: Optional[str]
    current_team: Optional[str]
    birth_year: Optional[int]
    preferred_foot: Optional[str]
    height: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "name": "Lionel Messi",
                "image_url": "https://example.com/messi.jpg",
                "current_team": "Inter Miami CF",
                "birth_year": 1987,
                "preferred_foot": "Left",
                "height": 170
            }
        }
