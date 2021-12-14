from pydantic import BaseModel
from database import Base


class CarsShortInfo(Base):
    model: str
    make: str

    class Config:
        orm_mode = True


class CarsPost(BaseModel):
    model: str
    make: str
    type: str
