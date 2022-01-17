from pydantic import BaseModel


class UserInfo(BaseModel):
    id: int
    email: str
    password: str

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True


class BrandCreate(BaseModel):
    brand: str


class BrandInfo(BaseModel):
    id: int
    brand: str

    class Config:
        orm_mode = True


class ModelCreate(BaseModel):
    model: str


class ModelInfo(BaseModel):
    id: int
    model: str

    class Config:
        orm_mode = True


class SettingsCreate(BaseModel):
    distance: str
    consumption: str
    user_id: int


class SettingsInfo(BaseModel):
    id: int
    consumption: str
    distance: str

    class Config:
        orm_mode = True


class CarCreate(BaseModel):
    year: int
    color: str
    brand_id: int
    model_id: int
    users_id: int


class CarInfo(BaseModel):
    id: int
    year: int
    color: str

    class Config:
        orm_mode = True


class MileageInfo(BaseModel):
    id: int
    mileage_max: int


    class Config:
        orm_mode = True


class MileageCreate(BaseModel):
    mileage_max: int
    car_id: int