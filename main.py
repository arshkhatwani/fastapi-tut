from fastapi import FastAPI
from router import blogs, users, articles, auth
from db import models
from db.database import engine


app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(articles.router)
app.include_router(blogs.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


models.Base.metadata.create_all(engine)
