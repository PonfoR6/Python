from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session, selectinload
from fastapi import status, HTTPException
import model
import schemas
from database import get_db


def all(mileage: int, consumption: int, db: Session = Depends(get_db)):
    if mileage < 0 or consumption < 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Enter valid amount (number must be 0 or higher)"
        )
    return db.query(model.Car) \
        .join(model.PostSettings) \
        .options(selectinload(model.Car.owner)) \
        .options(selectinload(model.Car.settings)) \
        .filter(model.PostSettings.consumption == consumption, model.PostSettings.mileage == mileage).all()


def create_car(request: schemas.CarCreate, user_id: int, db: Session = Depends(get_db)):
    new_settings = model.PostSettings(
        consumption=request.settings.consumption,
        mileage=request.settings.mileage
    )
    db.add(new_settings)
    db.commit()
    db.refresh(new_settings)
    new_car = model.Car(
        brand=request.brand,
        model=request.model,
        settings_id=new_settings.id,
        owner_id=user_id
    )
    db.add(new_car)
    db.commit()
    db.refresh(new_car)
    return new_car


def update_car(id: int, request: schemas.Car, db: Session):
    car = db.query(model.Car).filter(model.Car.id == id)

    if not car.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"car with id {id} not found"
        )

    car.update(request.dict())
    db.commit()
    return car.first()


def delete_car(id: int, request: schemas.CarCreate, db: Session):
    car = db.query(model.Car).filter(model.Car.id == id)

    if not car.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Car with id-{id} not found"
        )
    car.update(synchronize_session=False)
    db.commit()

    return {"details": "Success"}
