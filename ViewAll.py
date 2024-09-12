import mysql.connector
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="18082002",
        database="amdocsproject"
    )

def view_employee():
    db = connect_to_database()
    if db is None:
        return
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employee")
    results = cursor.fetchall()
    if results:
        print("\nEmployee Records:")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Department: {row[2]}, Age: {row[3]}, Email: {row[4]}")
    else:
        print("No employee records found.")
    cursor.close()
    db.close()

if __name__ == "__main__":
    view_employee()
