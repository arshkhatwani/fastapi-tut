from pydantic import BaseModel
from typing import List


class UserBase(BaseModel):
    name: str
    email: str
    password: str


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


class Article(BaseModel):
    title: str
    content: str
    published: bool


class UserDisplay(BaseModel):
    name: str
    email: str
    items: List[Article] = []

    # Working without this also
    # class Config:
    #     orm_mode = True


class ArticleUser(BaseModel):
    # User for ArticleDisplay
    id: int
    name: str
    email: str


class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: ArticleUser
