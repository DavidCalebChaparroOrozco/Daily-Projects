# Handles the display of the menu and employee data.
class EmployeeView:
    @staticmethod
    # Displays the main menu.
    def display_menu():
        print("\n🌟 Employee Management System by David Caleb🌟")
        print("1. View all employees")
        print("2. Add new employee")
        print("3. Remove employee")
        print("4. Search by department")
        print("5. Update employee salary")
        print("6. Show statistics")
        print("7. Save data")
        print("8. Load data")
        print("9. Exit")

    @staticmethod
    # Displays a list of employees.
    def display_employees(employees):
        if not employees:
            print("No employees found.")
        else:
            for emp in employees:
                print(emp)

    @staticmethod
    # Gets employee details from the user.
    def get_employee_details():
        id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        position = input("Enter employee position: ")
        salary = float(input("Enter employee salary: "))
        department = input("Enter employee department: ")
        return id, name, position, salary, department

    @staticmethod
    # Gets the employee ID from the user.
    def get_employee_id():
        return input("Enter employee ID: ")

    @staticmethod
    # Gets the new salary from the user.
    def get_new_salary():
        return float(input("Enter new salary: "))

    @staticmethod
    # Gets the department name from the user.
    def get_department():
        return input("Enter department name: ")

    @staticmethod
    # Displays employee statistics.
    def show_statistics(stats):
        print(f"Total Employees: {stats['total_employees']}")
        print(f"Total Salary: {stats['total_salary']}")
        print(f"Average Salary: {stats['average_salary']:.2f}")