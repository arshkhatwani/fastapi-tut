from fastapi import APIRouter, Depends
from schemas import ArticleDisplay, ArticleBase, ArticleUser
from db import db_article
from db.database import get_db
from auth.oauth2 import get_current_user

router = APIRouter(prefix='/articles', tags=['articles'])


@router.post('/')
def create_article(request: ArticleBase, db_session=Depends(get_db)):
    return db_article.create_article(db_session, request)


@router.get('/{id}')  # , response_model=ArticleDisplay)
def get_article(id: int, db_session=Depends(get_db), user: ArticleUser = Depends(get_current_user)):
    article = db_article.get_article(db_session, id)
    return {'article': article, 'current_user': user.name}
