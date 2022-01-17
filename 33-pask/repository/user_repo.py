from sqlalchemy.orm import Session
from fastapi import status, HTTPException
import schemas
import model


def get_all(db: Session):
    return db.query(model.User).all()


def create_user(request: schemas.UserCreate, db: Session):
    new_user = model.User(
        first_name=request.email,
        last_name=request.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def update_user(id: int, request: schemas.UserInfo, db: Session):
    user = db.query(model.User).filter(model.User.id == id)

    if not user.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )
    user.update(request.dict())
    db.commit()

    return user.first()


def delete_user(id: int, db: Session):
    user = db.query(model.User).filter(model.User.id == id)

    if not user.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )
    user.delete(synchronize_session=False)
    db.commit()

    return {"details": "Success"}