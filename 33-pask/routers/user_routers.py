from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
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


# @router.put('/update/{user_id}')
# def update_user(id: int, request: schemas.User, db: Session):
#     user = db.query(model.User).filter(model.User.id == id)
#
#     if not user.first():
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"User with id-{id} not found"
#         )
#     user.update(request.dict())
#     db.commit()
#
#     return user.first()
