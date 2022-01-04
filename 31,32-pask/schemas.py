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


class BlogSettingsCreate(BaseModel):
    is_active: bool


class BlogCreate(BaseModel):
    title: str
    body: str
    settings: BlogSettingsCreate


class SettingsSmallInfo(BaseModel):
    id: int
    title: str


class Blog(BaseModel):
    id: int
    title: str
    body: Optional[str] = None
    owner_id = int
    owner: Optional[UserSmallInfo]

    settings_id: int
    settings:SettingsSmallInfo
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
