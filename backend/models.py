from pydantic import BaseModel
from datetime import date

class Expense(BaseModel):
    date: date
    category: str
    amount: float
    payment_method : str
    description : str | None = None #optional


class User(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token :str
    token_type : str = "bearer"
