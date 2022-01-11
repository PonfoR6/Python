from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, selectinload
import model
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/cars',
    tags=['Cars']
)


@router.get('', )
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


@router.post('/create/{user_id}')
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


@router.put('/update/{car_id}')
def update_car(car_id: int, request: schemas.CarCreate, db: Session):
    post = db.query(model.Car).filter(model.Car.id == car_id)
