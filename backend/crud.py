from sqlalchemy.orm import Session
from .models import Expense
from .database_models import ExpenseDB

def add_expense(db:Session,expense_data:Expense):
    new_exp = ExpenseDB(
        date = expense_data.date,
        category = expense_data.category,
        amount = expense_data.amount,
        payment_method = expense_data.payment_method,
        description = expense_data.description
    )

    db.add(new_exp)
    db.commit()
    db.refresh(new_exp)
    return{"message":"Expense added Sucessfully!"}


def get_all_expenses(db:Session):
    return db.query(ExpenseDB).all()



def update_expense(db:Session,expense_id:int,expense_data:Expense):
    expense = db.query(ExpenseDB).filter(ExpenseDB.id==expense_id).first()

    if not expense:
        return {"error":"Expense not found"}
    
    expense.date = expense_data.date
    expense.category = expense_data.category
    expense.amount = expense_data.amount
    expense.payment_method = expense_data.payment_method
    expense.description = expense_data.description
    db.commit()
    return {"message":"Expense updated successfully!"}


def delete_expense(db:Session,expense_id:int):
    expense = db.query(ExpenseDB).filter(ExpenseDB.id==expense_id).first()

    if not expense:
        return {"error":"Expense not found"}
    
    db.delete(expense)
    db.commit()

    return {"message":"Expense delete sucessfully!"}
