# backend/models/transaction.py

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)  
    #user_id = Column(Integer, ForeignKey("user_id"), nullable=False) 
    user_id = Column(String(50), ForeignKey("users.user_id"), nullable=False)  #文字列へ修正

    image_path = Column(String(255), nullable=True)  # 画像データへのパス
    metric1_score = Column(Float, nullable=True)
    metric2_score = Column(Float, nullable=True)
    metric3_score = Column(Float, nullable=True)
    total_score = Column(Float, nullable=True)
    evaluated_at = Column(DateTime, nullable=False)

    # リレーションシップ
    user = relationship("User", back_populates="transactions")