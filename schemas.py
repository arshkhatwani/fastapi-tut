from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    password: str


class UserDisplay(BaseModel):
    name: str
    email: str

    # Working without this also
    class Config:
        orm_mode = True
