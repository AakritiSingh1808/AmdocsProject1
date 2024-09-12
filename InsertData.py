import mysql.connector

def insert_employee():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="18082002",
        database="amdocsproject"
    )

    cursorObject = database.cursor()
    emp_id = int(input("Enter Id: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    age = int(input("Enter Age: "))
    email = input("Enter Email: ")

    sql = "Insert into employee(Employee_Id, Name, Department, Age, Email)" \
          "Values (%s,%s,%s,%s,%s)"
    val=(emp_id,name,dept,age,email)

    cursorObject.execute(sql, val)
    print("Employee Data Inserted Successfully")
    database.commit()
    database.close()
