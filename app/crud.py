from sqlalchemy.orm import Session
from . import models, schemas

# User CRUD operations
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, name=user.name, mobile=user.mobile)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Expense CRUD operations
def create_expense(db: Session, expense: schemas.ExpenseCreate):
    db_expense = models.Expense(
        amount=expense.amount,
        description=expense.description,
        payer_id=expense.payer_id,
        split_method=expense.split_method,
        exact_amounts=expense.exact_amounts,
        percentages=expense.percentages
    )
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def get_user_expenses(db: Session, user_id: int):
    return db.query(models.Expense).filter(models.Expense.payer_id == user_id).all()

def get_all_expenses(db: Session):
    return db.query(models.Expense).all()

