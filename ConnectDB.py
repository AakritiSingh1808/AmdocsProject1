import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="18082002"
)

cursorObject = database.cursor()
cursorObject.execute("create database AmdocsProject")