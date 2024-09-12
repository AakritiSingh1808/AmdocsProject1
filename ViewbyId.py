import mysql.connector
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="18082002",
        database="amdocsproject"
    )
def view_employee_by_id(emp_id):
    #emp_id = int(input("Enter employee ID to view: "))
    db = connect_to_database()
    if db is None:
        return
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employee WHERE Employee_Id = %s", (emp_id,))
    result = cursor.fetchone()
    if result:
        print(f"ID: {result[0]}, Name: {result[1]}, Department: {result[2]}, Age: {result[3]}, Email: {result[4]}")
    else:
        print("No employee found with that ID.")
    cursor.close()
    db.close()
if __name__ == "__main__":
    view_employee_by_id()
