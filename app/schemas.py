from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    email: str
    name: str
    mobile: str

class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    mobile: str

    class Config:
        orm_mode = True

class ExpenseCreate(BaseModel):
    amount: float
    description: str
    payer_id: int
    split_method: str  # 'equal', 'exact', 'percentage'
    exact_amounts: Optional[dict]
    percentages: Optional[dict]

class ExpenseResponse(BaseModel):
    id: int
    amount: float
    description: str
    payer_id: int
    split_method: str
    exact_amounts: Optional[dict]
    percentages: Optional[dict]

    class Config:
        orm_mode = True

