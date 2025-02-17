from model.model import Employee, EmployeeModel
from view.view import EmployeeView

# Manages the interaction between the model and the view.
class EmployeeController:
    def __init__(self):
        self.model = EmployeeModel()
        self.view = EmployeeView()

    # Runs the employee management system.
    def run(self):
        while True:
            self.view.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.view_all_employees()
            elif choice == "2":
                self.add_employee()
            elif choice == "3":
                self.remove_employee()
            elif choice == "4":
                self.search_by_department()
            elif choice == "5":
                self.update_employee_salary()
            elif choice == "6":
                self.show_statistics()
            elif choice == "7":
                self.save_data()
            elif choice == "8":
                self.load_data()
            elif choice == "9":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    # Displays all employees.
    def view_all_employees(self):
        employees = self.model.get_all_employees()
        self.view.display_employees(employees)

    # Adds a new employee.
    def add_employee(self):
        id, name, position, salary, department = self.view.get_employee_details()
        employee = Employee(id, name, position, salary, department)
        self.model.add_employee(employee)
        print("Employee added successfully.")

    # Removes an employee.
    def remove_employee(self):
        employee_id = self.view.get_employee_id()
        self.model.remove_employee(employee_id)
        print("Employee removed successfully.")

    # Searches for employees by department.
    def search_by_department(self):
        department = self.view.get_department()
        employees = self.model.search_by_department(department)
        self.view.display_employees(employees)

    # Updates an employee's salary.
    def update_employee_salary(self):
        employee_id = self.view.get_employee_id()
        new_salary = self.view.get_new_salary()
        self.model.update_employee_salary(employee_id, new_salary)
        print("Salary updated successfully.")

    # Displays employee statistics.
    def show_statistics(self):
        stats = self.model.get_statistics()
        self.view.show_statistics(stats)

    # Saves employee data to a file.
    def save_data(self):
        with open("employees.txt", "w") as file:
            for emp in self.model.get_all_employees():
                file.write(f"{emp.id},{emp.name},{emp.position},{emp.salary},{emp.department}\n")
        print("Data saved successfully.")

    # Loads employee data from a file.
    def load_data(self):
        try:
            with open("employees.txt", "r") as file:
                for line in file:
                    id, name, position, salary, department = line.strip().split(",")
                    employee = Employee(id, name, position, float(salary), department)
                    self.model.add_employee(employee)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No data file found.")