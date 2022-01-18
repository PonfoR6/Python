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
    return repo.get(db)


@router.post('/create')
def user_create(request: schemas.UserCreate, db: Session = Depends(get_db)):
    return repo.create_user(request, db)


@router.put('/update/{id}')
def user_update(id: int, request: schemas.UserCreate, db: Session = Depends(get_db)):
    return repo.update_user(id, request, db)


@router.delete('/delete/{id}')
def user_delete(id: int, db: Session = Depends(get_db)):
    return repo.delete_user(id, db)
