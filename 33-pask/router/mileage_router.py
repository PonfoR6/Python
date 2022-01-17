from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from repository import mileage_repo as repo
from database import get_db
import schemas
from typing import List


router = APIRouter(
    prefix='/api/mileage',
    tags=['Mileage']
)


@router.get('', response_model=List[schemas.MileageInfo])
def all(db: Session = Depends(get_db)):
    return repo.get_all(db)


@router.post('/create')
def create_car(request: schemas.MileageCreate, db: Session = Depends(get_db)):
    return repo.create_mile(request, db)


@router.put('/update/{id}')
def update(id: int, request: schemas.MileageInfo, db: Session = Depends(get_db)):
    return repo.update_mile(id, request, db)


@router.delete('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    return repo.delete_mile(id, db)