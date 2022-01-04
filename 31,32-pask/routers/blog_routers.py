from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, selectinload
import model
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/blogs',
    tags=['Blogs']
)


@router.get('', )
def all(active: int, db: Session = Depends(get_db)):
    if active < 0 or active > 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Wrong active state passed"
        )
    return db.query(model.Blog) \
        .join(model.PostSettings) \
        .options(selectinload(model.Blog.owner)) \
        .options(selectinload(model.Blog.settings)) \
        .filter(model.PostSettings.is_active == active).all()


@router.post('/create/{user_id}')
def create_post(request: schemas.BlogCreate, user_id: int, db: Session = Depends(get_db)):
    new_settings = model.PostSettings(
        is_active=request.settings.is_active
    )
    db.add(new_settings)
    db.commit()
    db.refresh(new_settings)
    new_post = model.Blog(
        title=request.title,
        body=request.body,
        settings_id=new_settings.id,
        owner_id=user_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.put('/update/{post_id}')
def update_post(id: int, request: schemas.CarsPost, db: Session):
    post = db.query(model.Blog).filter(model.Blog.id == post_id)
    settings = db.query(models.PostSettings).filter(models.PostSettings.id == post.settings_id)

    if not car.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Human with id {id} not found"
        )
    car.update(request.dict())
    db.commit()

    return car.first()
