from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from repository import user_repo as repo
from database import get_db
import schemas
from typing import List

router = APIRouter(
    prefix='/api/users',
    tags=['Users']
)


@router.get('', response_model=List[schemas.UserInfo])
def all(db: Session = Depends(get_db)):
    return repo.get_all(db)


@router.post('/create')
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    return repo.create_user(request, db)


@router.put('/update/{id}')
def update(id: int, request: schemas.UserCreate, db: Session = Depends(get_db)):
    return repo.update_user(id, request, db)


@router.delete('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    return repo.delete_user(id, db)
