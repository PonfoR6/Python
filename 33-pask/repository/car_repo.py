from sqlalchemy.orm import Session
from fastapi import status, HTTPException
import schemas
import model


def get_all(db: Session):
    return db.query(model.Car).all()


def create_car(request: schemas.CarCreate, db: Session):
    new_car = model.Car(
        year=request.year,
        color=request.color,
        brand_id=request.brand_id,
        model_id=request.model_id,
        users_id=request.users_id
    )
    db.add(new_car)
    db.commit()
    db.refresh(new_car)
    return new_car


def update_car(id: int, request: schemas.CarCreate, db: Session):
    car = db.query(model.Car).filter(model.Car.id == id)

    if not car.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Car with id {id} not found"
        )

    car.update(request.dict())
    db.commit()
    return car.first()


def delete_car(id: int, db: Session):
    car = db.query(model.Car).filter(model.Car.id == id)

    if not car.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Car with id {id} not found"
        )
    car.delete(synchronize_session=False)
    db.commit()

    return {"details": "Success"}