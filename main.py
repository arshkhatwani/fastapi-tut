from fastapi import FastAPI
from router import blogs

app = FastAPI()

app.include_router(blogs.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
