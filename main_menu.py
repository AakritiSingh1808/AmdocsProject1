import mysql.connector
import InsertData
import ViewAll
import ViewbyId
import UpdateEmp
import DeleteEmp

def get_db_password():
    username = input("Enter MySQL username: ")
    password = input("Enter MySQL database password: ")
    return username, password

def connect_to_database(username, password):
    try:
        return mysql.connector.connect(
            host="localhost",
            user=username,
            passwd=password,
            database="amdocsproject"
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
def show_menu():
    print("\n--- Employee Management System ---")
    print("1. Insert Employee")
    print("2. View Employees")
    print("3. View Employee by ID")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

def main():
    username, password = get_db_password()
    db = connect_to_database(username, password)

    if db is None:
        print("Unable to connect to the database. Exiting...")
        return

    while True:
        try:
            show_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                InsertData.insert_employee()
            elif choice == '2':
                ViewAll.view_employee()
            elif choice == '3':
                emp_id = input("Enter employee ID: ")
                ViewbyId.view_employee_by_id(emp_id)
            elif choice == '4':
                UpdateEmp.update_employee()
            elif choice == '5':
                DeleteEmp.delete_employee()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
