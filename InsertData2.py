import mysql.connector
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="18082002",
        database="amdocsproject"
    )

def insert_default_data():
    db = connect_to_database()
    cursor = db.cursor()

    employee = [
        (3,"Ravi Kumar", "HR",24, "ravi.kumar@example.com"),
        (4,"Priya Sharma", "Finance", 23, "priya.sharma@example.com"),
        (5,"Amit Verma", "IT", 29, "amit.verma@example.com"),
        (6,"Sneha Patel", "Marketing", 22, "sneha.patel@example.com"),
        (7,"Rajesh Singh", "Sales", 27, "rajesh.singh@example.com")
    ]

    sql = "INSERT INTO employee (Employee_Id, Name, Department, Age, email) VALUES (%s,%s, %s, %s, %s)"
    cursor.executemany(sql, employee)
    db.commit()
    print(f"{cursor.rowcount} employees inserted successfully.")

    cursor.close()
    db.close()

if __name__ == "__main__":
    insert_default_data()
