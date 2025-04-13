from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    email: str


users: List[User] = []


@app.get("/")
def read_root():
    return {"message": "FastAPI app running..."}


@app.get("/users")
def get_users():
    return users


@app.post("/user")
def add_user(user: User):
    users.append(user)
    return user
