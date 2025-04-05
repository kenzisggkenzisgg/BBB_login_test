# backend/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ローカルMySQLの設定 mysql+pymysql://<ユーザー名>:<パスワード>@<ホスト名>:<ポート番号>/<データベース名>
DATABASE_URL = "mysql+pymysql://root:mysql/<yourpassword>@localhost:3306/login_test"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
