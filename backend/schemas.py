# backend/schemas.py

from pydantic import BaseModel

class UserCreate(BaseModel):
    user_id: str
    email: str
    password: str

class UserLogin(BaseModel):
    user_id: str
    password: str

