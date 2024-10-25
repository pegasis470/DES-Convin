from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud, models
from ..database import get_db

router = APIRouter()

@router.post("/expenses/", response_model=schemas.ExpenseResponse)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db=db, expense=expense)

@router.get("/expenses/user/{user_id}", response_model=List[schemas.ExpenseResponse])
def get_user_expenses(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_expenses(db=db, user_id=user_id)

@router.get("/expenses/", response_model=List[schemas.ExpenseResponse])
def get_all_expenses(db: Session = Depends(get_db)):
    return crud.get_all_expenses(db=db)

