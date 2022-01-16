from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import repository.car_repository
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/cars',
    tags=['Cars']
)


@router.get('', )
def all_router(mileage: int, consumption: int, db: Session = Depends(get_db)):
    return repository.car_repository.all(mileage, consumption, db)


@router.post('/create/{user_id}')
def create_car_router(request: schemas.CarCreate, user_id: int, db: Session = Depends(get_db)):
    return repository.car_repository.create_car(request, user_id, db)


@router.put('/update/{car_id}')
def update_car_router(id: int, request: schemas.Car, db: Session):
    return repository.car_repository.update_car(id, request, db)


@router.delete('/update/{id}')
def delete_car_router(id: int, db: Session = Depends(get_db)):
    return repository.car_repository.delete_car(id, db)
