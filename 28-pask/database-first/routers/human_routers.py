from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
import modelis

import schemas
from database import get_db

router = APIRouter(
    prefix='/api/human',
    tags=['Human']
)


@router.get('')
def all(db: Session = Depends(get_db)):
    humans = db.query(modelis.Human).all()
    return humans


@router.post('')
def create(request: schemas.HumansShortInfo, db: Session = Depends(get_db)):
    new_human = modelis.Human(
        first_name=request.first_name,
        last_name=request.last_name,
        email='qwe@qwe.qwe'
    )
    db.add(new_human)
    db.commit()
    db.refresh(new_human)

    return new_human