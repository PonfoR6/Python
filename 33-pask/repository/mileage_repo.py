from sqlalchemy.orm import Session
from fastapi import status, HTTPException
import schemas
import model


def get_all(db: Session):
    return db.query(model.Mileage).all()


def create_mile(request: schemas.MileageCreate, db: Session):
    new_mileage = model.Mileage(
        mileage_max=request.mileage_max,
        car_id=request.car_id
    )

    db.add(new_mileage)
    db.commit()
    db.refresh(new_mileage)
    return new_mileage


def update_mile(id: int, request: schemas.MileageCreate, db: Session):
    mileage = db.query(model.Mileage).filter(model.Mileage.id == id)

    if not mileage.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Mileage with id {id} not found"
        )
    mileage.update(request.dict())
    db.commit()

    return mileage.first()


def delete_mile(id: int, db: Session):
    mileage = db.query(model.Mileage).filter(model.Mileage.id == id)

    if not mileage.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Mileage with id {id} not found"
        )
    mileage.delete(synchronize_session=False)
    db.commit()

    return {"details": "Success"}
