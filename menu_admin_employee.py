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


def authenticate_user():
    role = None
    employee_id = None
    print("\n--- Login ---")
    username = input("Enter username (admin/employee): ")

    if username == "admin":
        role = "admin"
        password = input("Enter admin password: ")
        if password == "1808":
            print("Admin login successful!")
        else:
            print("Incorrect admin password.")
            return None, None
    else:
        role = "employee"
        password = input("Enter employee password: ")
        employee_id = input("Enter your employee ID: ")

        if password == "2002":
            print(f"Employee (ID: {employee_id}) login successful!")
        else:
            print("Incorrect employee password.")
            return None, None
    return role, employee_id


def show_admin_menu():
    print("\n--- Admin Menu ---")
    print("1. Insert Employee")
    print("2. View Employees")
    print("3. View Employee by ID")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")


def show_employee_menu():
    print("\n--- Employee Menu ---")
    print("1. View Employees")
    print("2. View Employee by ID")
    print("3. Update My Data")
    print("4. Exit")


def main():
    username, password = get_db_password()
    db = connect_to_database(username, password)

    if db is None:
        print("Unable to connect to the database. Exiting...")
        return

    role, employee_id = authenticate_user()

    if role == "admin":
        while True:
            show_admin_menu()
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

    elif role == "employee":
        while True:
            show_employee_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                ViewAll.view_employee()
            elif choice == '2':
                emp_id = input("Enter employee ID: ")
                ViewbyId.view_employee_by_id(emp_id)
            elif choice == '3':  # Update employee's own data
                UpdateEmp.update_employee(employee_id)
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
