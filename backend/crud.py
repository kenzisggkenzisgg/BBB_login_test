# backend/crud.py

from fastapi import HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from .models.user import User  # ← モデルを明示的にインポート
from . import schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_user(db: Session, user_data: schemas.UserCreate):  # ← 引数名を user_data に変更
    if db.query(User).filter(User.email == user_data.email).first():
        raise HTTPException(status_code=400, detail="このメールアドレスは既に登録されています")
    if db.query(User).filter(User.user_id == user_data.user_id).first():
        raise HTTPException(status_code=400, detail="このユーザーIDは既に使用されています")

    hashed_password = get_password_hash(user_data.password)
    db_user = User(
        user_id=user_data.user_id,
        email=user_data.email,
        hashed_password=hashed_password,
        birth_date=user_data.birth_date
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_user_id(db: Session, user_id: str):
    return db.query(User).filter(User.user_id == user_id).first()


