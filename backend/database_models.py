from sqlalchemy import Column,Integer,String,Float,Date
from backend.database import Base

class ExpenseDB(Base):
    __tablename__ = "expenses"

    id = Column(Integer,primary_key=True,index=True)
    date = Column(Date,nullable=False)
    category = Column(String,nullable=False)
    amount = Column(Float,nullable=False)
    payment_method = Column(String,nullable=False)
    description =Column(String,nullable=True)

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,nullable=False)
    hashpassword = Column(String,nullable=False)
