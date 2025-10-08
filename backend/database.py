import pymysql
from pymysql.cursors import DictCursor

DB_HOST = "localhost"
DB_USER = "root"  
DB_PASSWORD = "laadruturaj@01" 
DB_NAME = "expense_tracker"


def create_connection():
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD, 
            database= DB_NAME
        )
        print("Database created Successfully!")
    except pymysql.MySQLError as e:
        print(f"❌ Error connecting to database: {e}")
        return None
    
if __name__ == "__main__":
    conn = create_connection()
    if conn:
        conn.close()