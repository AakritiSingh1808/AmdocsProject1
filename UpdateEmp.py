import mysql.connector
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="18082002",
        database="amdocsproject"
    )

def update_employee(emp_id):
    # Employee_Id = int(input("Enter employee ID to update: "))
    db = connect_to_database()
    if db is None:
        return
    cursor = db.cursor()

    cursor.execute("SELECT * FROM employee WHERE Employee_Id = %s", (emp_id,))
    result = cursor.fetchone()

    if result:
        print(f"Current details: ID: {result[0]}, Name: {result[1]}, Department: {result[2]}, Age: {result[3]}, Email: {result[4]}")

        Name = input("Enter new name (or leave blank to keep current): ") or result[1]
        Department = input("Enter new department (or leave blank to keep current): ") or result[2]
        Age = input("Enter new age (or leave blank to keep current): ") or result[3]
        Email = input("Enter new email (or leave blank to keep current): ") or result[4]

        sql = """UPDATE employee SET Name = %s, Department = %s, Age = %s, Email = %s WHERE Employee_Id = %s"""
        cursor.execute(sql, (Name, Department, Age, Email, emp_id))

        db.commit()
        print("Employee details updated successfully.")
    else:
        print("No employee found with that ID.")

    cursor.close()
    db.close()

if __name__ == "__main__":
    update_employee()
