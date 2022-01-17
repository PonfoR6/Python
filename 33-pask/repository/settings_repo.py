from sqlalchemy.orm import Session
from fastapi import status, HTTPException
import schemas
import model


def get_all(db: Session):
    return db.query(model.Settings).all()


def create_settings(request: schemas.SettingsCreate, db: Session):
    global id
    new_settings = model.Settings(
        odometer=request.distance,
        consumption=request.consumption,
        user_id=request.user_id
    )
    db.add(new_settings)
    db.commit()
    db.refresh(new_settings)
    return new_settings


def update_settings(id: int, request: schemas.SettingsCreate, db: Session):
    settings = db.query(model.Settings).filter(model.Settings.id == id)

    if not settings.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Settings with id {id} not found"
        )

    settings.update(request.dict())
    db.commit()

    return settings.first()


def delete_settings(id: int, db: Session):
    settings = db.query(model.Settings).filter(model.Settings.id == id)

    if not settings.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Settings with id {id} not found"
        )
    settings.delete(synchronize_session=False)
    db.commit()

    return {"details": "Success"}
