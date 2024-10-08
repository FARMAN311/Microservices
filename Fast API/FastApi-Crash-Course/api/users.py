import fastapi
from fastapi import FastAPI, Path, Query
from typing import List, Optional
from pydantic import BaseModel


router = fastapi.APIRouter()

users = []

class User(BaseModel):
    email : str
    is_active : bool
    bio : Optional[str]

@router.get("/user",response_model=List[User])
async def get_user():
    return users

@router.post("/users")
async def create_user(user:User):
    users.append(user)
    return 'Sucess'

@router.get('/user/{id}')
async def get_user(
    id : int ,
    q : str
    ): 
    return {"user":users[id], "query":q}

