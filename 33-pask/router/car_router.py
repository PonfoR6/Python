from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from repository import car_repo as repo
from database import get_db
import schemas
from typing import List

router = APIRouter(
    prefix='/api/cars',
    tags=['Cars']
)


@router.get('', response_model=List[schemas.CarInfo])
def all(db: Session = Depends(get_db)):
    return repo.get(db)


@router.post('/create')
def car_create(request: schemas.CarCreate, db: Session = Depends(get_db)):
    return repo.create_car(request, db)


@router.put('/update/{id}')
def car_update(id: int, request: schemas.CarCreate, db: Session = Depends(get_db)):
    return repo.update_car(id, request, db)


@router.delete('/delete/{id}')
def car_delete(id: int, db: Session = Depends(get_db)):
    return repo.delete_car(id, db)
