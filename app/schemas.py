from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class PostCreate(BaseModel):
    caption: str

class PostResponse(BaseModel):
    id: UUID
    caption: str
    url: str
    created_at: datetime

    class Config:
        from_attributes = True