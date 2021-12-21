from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import model
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/blogs',
    tags=['Blogs']
)


@router.get('', response_model=List[schemas.Blog])
def all(db: Session = Depends(get_db)):
    return db.query(model.Blog).all()


@router.post('/create/{user_id}')
def create_post(request: schemas.BlogCreate, user_id: int, db: Session = Depends(get_db)):
    new_post = model.Blog(
        title=request.title,
        body=request.body,
        tags=request.tags,
        owner_id=user_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
