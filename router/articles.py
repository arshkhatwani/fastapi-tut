from fastapi import APIRouter, Depends
from schemas import ArticleDisplay, ArticleBase
from db import db_article
from db.database import get_db

router = APIRouter(prefix='/articles', tags=['articles'])


@router.post('/')
def create_article(request: ArticleBase, db_session=Depends(get_db)):
    return db_article.create_article(db_session, request)


@router.get('/{id}', response_model=ArticleDisplay)
def get_article(id: int, db_session=Depends(get_db)):
    article = db_article.get_article(db_session, id)
    return article
