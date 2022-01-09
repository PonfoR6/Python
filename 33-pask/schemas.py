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


class CarSettingsCreate(BaseModel):
    pass


class CarCreate(BaseModel):
    brand: str
    model: str
    settings: CarSettingsCreate


class SettingsSmallInfo(BaseModel):
    id: int
    brand: str


class Car(BaseModel):
    id: int
    brand: str
    model: Optional[str] = None
    owner_id = int
    owner: Optional[UserSmallInfo]

