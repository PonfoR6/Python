from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from repository import brand_repo as repo
from database import get_db
import schemas
from typing import List

router = APIRouter(
    prefix='/api/brands',
    tags=['Brands']
)


@router.get('', response_model=List[schemas.BrandInfo])
def all(db: Session = Depends(get_db)):
    return repo.get(db)


@router.post('/create')
def brand_router(request: schemas.BrandCreate, db: Session = Depends(get_db)):
    return repo.create_brand(request, db)


@router.put('/update/{id}')
def brand_update(id: int, request: schemas.BrandCreate, db: Session = Depends(get_db)):
    return repo.update_brand(id, request, db)


@router.delete('/delete/{id}')
def brand_delete(id: int, db: Session = Depends(get_db)):
    return repo.delete_brand(id, db)
