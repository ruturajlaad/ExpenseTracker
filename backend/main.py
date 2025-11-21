from fastapi import FastAPI ,HTTPException,Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm


from backend.database import get_db
from backend.models import Expense,User
from backend.database_models import UserDB
from backend.crud import add_expense,delete_expense,update_expense,delete_expense,get_all_expenses
from backend.auth import hash_password,verify_password,create_access_token,get_current_user


app = FastAPI()

################################AUTH##################################
@app.post("/signup")
def signup(user:User,db:Session=Depends(get_db)):
    existing_user = db.query(UserDB).filter(UserDB.username==user.username).first()

    if existing_user:
        raise HTTPException(status_code=400,detail="UserName Already Exists.")
    
    new_user = UserDB(
        username=user.username,
        hashpassword=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    return{"message":"User Created Successfully!"}


@app.post("/login")
def login(form_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.username==form_data.username).first()

    if not user or not verify_password(form_data.password,user.hashpassword):
        raise HTTPException(status=401,detail="Invalid username or password")
    
    token = create_access_token({"sub":user.username})
    return{"access_token":token,"token_type":"bearer"}

######################################################################



#################################CRUD#########################################
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




