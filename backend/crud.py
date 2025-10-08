from backend.database import create_connection
from backend.models import Expense

#add new exp
def add_expense(expense_data: Expense):
    connection = create_connection()
    if connection:
        with connection.cursor() as cursor:
            sql= """
                INSERT INTO expenses(date,category,amount,payment_method,description)
                Values(%s,%s,%s,%s,%s)    
                """
            cursor.execute(sql,(
                expense_data.date,
                expense_data.category,
                expense_data.amount,
                expense_data.payment_method,
                expense_data.description             
            ))
            connection.commit()
        connection.close()
        return {"message": " Expense added successfully!"}
    return {"error": "Failed to add expense"}
#fetch all exp

def get_all_expenses():
    connection = create_connection()
    if connection:
        with connection.cursor() as cursor:
            cursor.execute("Select * from expenses")
            expenses = cursor.fetchall()
        connection.close()
        return expenses
    return []

#update an expense

def update_expense(expense_id: int, expense_data : Expense):
    connection = create_connection()
    if connection:
        with connection.cursor as cursor:
            sql = """
                UPDATE expenses
                SET date = %s, category = %s, amount = %s, payment_method = %s, description = %s
                WHERE id = %s
                """
            cursor.execute(sql,(
                expense_data.date,
                expense_data.category,
                expense_data.amount,
                expense_data.payment_method,
                expense_data.description,
                expense_id
            ))
            connection.commit()
        connection.close()
        return {"message": "Expense updated successfully!"}
    return {"error": "Failed to update expense"}

#Delete
def delete_expense(expense_id:int):
    connection = create_connection()
    if connection:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM expenses WHERE id = %s", (expense_id,))
            connection.commit()
        connection.close()
        return {"message": "Expense delete successfully!"}
    return {"error": "Failed to delete expense"}
