from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from fastapi_users import schemas

class PostCreate(BaseModel):
    title: str
    content: str

class PostResponse(BaseModel):
    id: UUID
    caption: str
    url: str
    created_at: datetime

    class Config:
        from_attributes = True


class UserRead(schemas.BaseUser[UUID]):
    pass

class UserCreate(schemas.BaseUserCreate):
    pass

class UserUpdate(schemas.BaseUserUpdate):
    pass

