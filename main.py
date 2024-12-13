from fastapi import FastAPI
from router import blogs
from db import models
from db.database import engine


app = FastAPI()

app.include_router(blogs.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


models.Base.metadata.create_all(engine)
