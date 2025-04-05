# backend/crud.py

from fastapi import HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from . import models, schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_user(db: Session, user: schemas.UserCreate):
    if db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(status_code=400, detail="このメールアドレスは既に登録されています")
    if db.query(models.User).filter(models.User.user_id == user.user_id).first():
        raise HTTPException(status_code=400, detail="このユーザーIDは既に使用されています")

    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        user_id=user.user_id,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_user_id(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.user_id == user_id).first()


