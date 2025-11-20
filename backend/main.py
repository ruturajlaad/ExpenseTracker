from fastapi import FastAPI ,HTTPException,Depends
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models import Expense
from backend.crud import add_expense,delete_expense,update_expense,delete_expense,get_all_expenses

app = FastAPI()

@app.post("/expenses")
def create_expense(expense:Expense,db:Session = Depends(get_db)):
    result = add_expense(db, expense)
    if "error" in result:
        raise HTTPException(status_code=400,detail=result["error"])
    return result

@app.get("/expenses")
def modify_expense(db:Session=Depends(get_db)):
    return get_all_expenses(db)


@app.put("/expenses/{expense_id}")
def update_expense_endpoint(expense_id:int,expense:Expense,db:Session= Depends(get_db)):
    result= update_expense(db,expense_id,expense)
    if "error" in result:
        raise HTTPException(status_code=400,detail=result["error"])
    return result


@app.delete("/expenses/{expense_id}")
def delete_expense_endpoint(expense_id:int,db:Session=Depends(get_db)):
    result = delete_expense(db,expense_id)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result




