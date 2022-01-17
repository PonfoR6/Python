from sqlalchemy.orm import Session
from fastapi import status, HTTPException
import schemas
import model



def get_all(db: Session):
    return db.query(model.Brand).all()


def create_brand(request: schemas.BrandCreate, db: Session):
    new_brand = model.Brand(
        brand=request.brand
    )

    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)
    return new_brand


def update_brand(id: int, request: schemas.BrandCreate, db: Session):
    brand = db.query(model.Brand).filter(model.Brand.id == id)

    if not brand.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Brand with id {id} not found"
        )
    brand.update(request.dict())
    db.commit()
    return brand.first()


def delete_brand(id: int, db: Session):
    brand = db.query(model.Brand).filter(model.Brand.id == id)

    if not brand.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Brand with id {id} not found"
        )
    brand.delete(synchronize_session=False)
    db.commit()

    return {"details": "Success"}