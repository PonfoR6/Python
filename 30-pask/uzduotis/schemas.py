from pydantic import BaseModel
from database import Base


class CarsShortInfo(Base):
    Topic: str
    Active_members: int

    class Config:
        orm_mode = True


class CarsPost(BaseModel):
    Topic: str
    Active_members: int
    Comments: int
