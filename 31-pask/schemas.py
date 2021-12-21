from typing import List, Optional
from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str


class UserSmallInfo(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True


class BlogCreate(BaseModel):
    title: str
    body: str
    tags: str


class Blog(BaseModel):
    id: int
    title: str
    body: Optional[str] = None
    tags: Optional[str] = None
    owner_id = int
    owner: Optional[UserSmallInfo]

    # Add owner here

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int
    email: str
    password: str

    blogs: List[Blog] = []

    class Config:
        orm_mode = True
