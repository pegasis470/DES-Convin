from sqlalchemy import Column, Integer, String, Float, ForeignKey,JSON
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    mobile = Column(String, unique=True)

    expenses = relationship("Expense", back_populates="payer")

class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    description = Column(String)
    payer_id = Column(Integer, ForeignKey('users.id'))
    
    # Split types
    split_method = Column(String)
    exact_amounts = Column(JSON, nullable=True)  # JSON: {"user_id": amount}
    percentages = Column(JSON, nullable=True)  # JSON: {"user_id": percentage}

    payer = relationship("User", back_populates="expenses")

