# Represents an employee with basic attributes.
class Employee:
    def __init__(self, id, name, position, salary, department):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.department = department

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Department: {self.department}"


# Manages the list of employees and provides CRUD operations.
class EmployeeModel:
    def __init__(self):
        self.employees = []  # List to store employees

    # Adds a new employee to the list.
    def add_employee(self, employee):
        self.employees.append(employee)

    # Removes an employee by their ID.
    def remove_employee(self, employee_id):
        self.employees = [emp for emp in self.employees if emp.id != employee_id]

    # Returns a list of all employees.
    def get_all_employees(self):
        return self.employees

    # Searches for employees by department.
    def search_by_department(self, department):
        return [emp for emp in self.employees if emp.department.lower() == department.lower()]

    # Updates an employee's salary by their ID.
    def update_employee_salary(self, employee_id, new_salary):
        for emp in self.employees:
            if emp.id == employee_id:
                emp.salary = new_salary
                break

    # Returns basic statistics about employees.
    def get_statistics(self):
        total_employees = len(self.employees)
        total_salary = sum(emp.salary for emp in self.employees)
        avg_salary = total_salary / total_employees if total_employees > 0 else 0
        return {
            "total_employees": total_employees,
            "total_salary": total_salary,
            "average_salary": avg_salary
        }