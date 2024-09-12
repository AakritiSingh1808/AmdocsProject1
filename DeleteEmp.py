import mysql.connector
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="18082002",
        database="amdocsproject"
    )

def delete_employee():
    emp_id = int(input("Enter employee ID to delete: "))
    db = connect_to_database()
    if db is None:
        return
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employee WHERE Employee_Id = %s", (emp_id,))
    result = cursor.fetchone()
    if result:
        cursor.execute("DELETE FROM employee WHERE Employee_Id = %s", (emp_id,))
        db.commit()
        print("Employee deleted successfully.")
    else:
        print("No employee found with that ID.")
    cursor.close()
    db.close()


if __name__ == "__main__":
    delete_employee()