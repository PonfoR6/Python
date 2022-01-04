from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import model
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/users',
    tags=['Users']
)


@router.get('', response_model=List[schemas.User])
def all(db: Session = Depends(get_db)):
    return db.query(model.User).all()


@router.post('/create')
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = model.User(
        email=request.email,
        password=request.password,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
