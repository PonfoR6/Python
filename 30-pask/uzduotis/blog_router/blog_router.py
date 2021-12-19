from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
import model
from blog_repo import blog_repository as repo
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/blog',
    tags=['Blog']
)


@router.get('', response_model=List[schemas.CarsShortInfo])
def all(db: Session = Depends(get_db)):
    return repo.get_car_short_info(db)


@router.get('/{id}', response_model=schemas.CarsShortInfo)
def get_single(id: int, db: Session = Depends(get_db)):
    return repo.get_car_single_short_info(id, db)


@router.post('')
def create(request: schemas.CarsShortInfo, db: Session = Depends(get_db)):
    return repo.create_car(request, db)


@router.put('/update/{id}')
def update(id: int, request: schemas.CarsPost, db: Session = Depends(get_db)):
    return repo.update_car(id, request, db)


@router.delete('/update/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    return repo.delete_car(id, db)
