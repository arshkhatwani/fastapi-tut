from pydantic import BaseModel


class BlogModel(BaseModel):
    id: int
    title: str
    available: bool
