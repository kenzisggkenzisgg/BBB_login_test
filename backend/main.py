# backend/main.py

from fastapi import FastAPI, Depends, HTTPException, Header, status
from sqlalchemy.orm import Session

from .models import user
from . import schemas, crud, auth
from .database import SessionLocal, engine, Base
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from .models import transaction  # ← 追記


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, user)
    return {"message": "ユーザー登録成功", "user_id": db_user.user_id}

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_user_id(db, user.user_id)
    if not db_user or not crud.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="ユーザーIDまたはパスワードが間違っています")
    
    
    # 🌟 最終ログイン日時を現在時刻に更新
    db_user.last_login_at = datetime.utcnow()
    db.commit()

    token = auth.create_access_token({"sub": db_user.user_id})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/protected")
def protected_route(authorization: str = Header(..., alias="Authorization")):
    token = authorization.replace("Bearer ", "")
    payload = auth.verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="無効なトークンです")
    return {"message": f"{payload['sub']} さん、ようこそ！"}

@app.post("/transactions")
def create_transaction(tran: schemas.TransactionCreate, db: Session = Depends(get_db)):
    db_tran = transaction.Transaction(**tran.dict())
    db.add(db_tran)
    db.commit()
    db.refresh(db_tran)
    return {"message": "トランザクションを登録しました", "transaction_id": db_tran.id}

