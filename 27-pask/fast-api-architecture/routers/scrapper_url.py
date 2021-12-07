from fastapi import FastAPI, APIRouter

from repository import scrapper_repository as repo

router = APIRouter(
    prefix='/api/scrap',
    tags=['Scrapper']
)


@router.get('/')
def hello():
    return repo.hello()