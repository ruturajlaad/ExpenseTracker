from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import create_engine


db_url = "postgresql://postgres:ruturaj@localhost:5432/expensetracker"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit = False, autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()