from pydantic import BaseModel
from datetime import date

class Expense(BaseModel):
    date: date
    category: str
    amount: float
    payment_method : str
    description : str | None = None #optional