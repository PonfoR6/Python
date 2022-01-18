from sqlalchemy.orm import Session
from fastapi import status, HTTPException
import schemas
import model


def get(db: Session):
    return db.query(model.Model).all()


def create_model(request: schemas.ModelInfo, db: Session):
    new_model = model.Model(
        car_model=request.model
    )
    db.add(new_model)
    db.commit()
    db.refresh(new_model)
    return new_model


def update_model(id: int, request: schemas.ModelCreate, db: Session):
    car_model = db.query(model.Model).filter(model.Model.id == id)

    if not car_model.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Model with id {id} not found"
        )
    car_model.update(request.dict())
    db.commit()

    return car_model.first()


def delete_model(id: int, db: Session):
    car_model = db.query(model.Model).filter(model.Model.id == id)

    if not car_model.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Model with id {id} not found"
        )
    car_model.delete(synchronize_session=False)
    db.commit()

    return {"details": "Success"}
