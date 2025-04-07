# backend/schemas.py

from pydantic import BaseModel, EmailStr
from datetime import date
from datetime import datetime
from typing import Optional #追記

class UserCreate(BaseModel):
    user_id: str
    email: str
    password: str
    birth_date: date  # ← 追加

class UserLogin(BaseModel):
    user_id: str
    password: str
    
class TransactionCreate(BaseModel):
    #user_id: int
    user_id: str  #修正
    image_path: Optional[str] = None
    metric1_score: Optional[float] = None
    metric2_score: Optional[float] = None
    metric3_score: Optional[float] = None
    total_score: Optional[float] = None
    evaluated_at: datetime

