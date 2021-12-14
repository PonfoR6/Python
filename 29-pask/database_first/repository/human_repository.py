from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from fastapi import status, HTTPException
import models
import schemas
from database import get_db


def get_car_short_info(db: Session):
    return db.query(models.Cars).all()


def get_car_single_short_info(db: Session, id: int):
    car = db.query(models.Cars).filter(models.Cars.id == id).first()

    if not car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Car with id {id} not found"
        )


def create_car(request: schemas.CarsPost, db: Session):
    new_car = models.Cars(
        first_name=request.make,
        last_name=request.model,
        email='qweqwe@qwe.com'
    )
    db.add(new_car)
    db.commit()
    db.refresh(new_car)

    return new_car


def update_car(id: int, request: schemas.CarsPost, db: Session):
    car = db.query(models.Cars).filter(models.Cars.id == id)

    if not car.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Human with id {id} not found"
        )
    car.update(request.dict())
    db.commit()

    return car.first()


def delete_car(id: int, request: schemas.CarsPost, db: Session):
    car = db.query(models.Cars).filter(models.Cars.id == id)

    if not car.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Human with id {id} not found"
        )
    car.update(synchronize_session=False)
    db.commit()

    return {"details": "Success"}
