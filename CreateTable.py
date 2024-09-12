import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="18082002",
    database="AmdocsProject"
)

cursorObject = database.cursor()

studentRecord = """Create Table Employee(
    Employee_Id int not null,
    Name Varchar(50) not null,
    Deptartment Varchar(50),
    Age int,
    Email varchar(50))
    """
cursorObject.execute(studentRecord)
database.close()
