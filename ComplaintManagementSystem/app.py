# Importing necessary libraries
from datetime import datetime

# Class Complaint
class Complaint:
    def __init__(self, code, complainant, accused, date, type):
        self.code = code
        self.complainant = complainant
        self.accused = accused
        self.date = date
        self.type = type

    def get_code(self):
        return self.code

    def set_date(self, date):
        self.date = date

    def __str__(self):
        return f'Code: {self.code}, Complainant: {self.complainant}, Accused: {self.accused}, Date: {self.date}, Type: {self.type}'

# Node class for linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Complaint List Class
class ComplaintList:
    def __init__(self):
        self.head = None

    def add(self, complaint):
        new_node = Node(complaint)
        new_node.next = self.head
        self.head = new_node

    def remove(self, code):
        current = self.head
        prev = None
        while current is not None and current.data.get_code() != code:
            prev = current
            current = current.next
        if current is None:
            return False
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next
        return True

    def complaints_by_person(self, name):
        result = []
        current = self.head
        while current is not None:
            if current.data.complainant == name or current.data.accused == name:
                result.append(current.data)
            current = current.next
        return result

    def percentage_by_type(self, type):
        count_type = 0
        total = 0
        current = self.head
        while current is not None:
            total += 1
            if current.data.type == type:
                count_type += 1
            current = current.next
        if total == 0:
            return 0.0
        return (count_type / total) * 100

    def show_complaints(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def set_date(self, code, new_date):
        current = self.head
        while current is not None:
            if current.data.get_code() == code:
                current.data.set_date(new_date)
                return True
            current = current.next
        return False

# Menu functions
def menu():
    complaint_list = ComplaintList()
    while True:
        print("\nComplaint Management Menu")
        print("1. Create complaint")
        print("2. Remove complaint")
        print("3. Create sublist of complaints by a person")
        print("4. Percentage of each type of complaint")
        print("5. Show complaints")
        print("6. Modify complaint date")
        print("7. Exit")
        option = input("Select an option: ")

        if option == "1":
            code = int(input("Code: "))
            complainant = input("Complainant: ")
            accused = input("Accused: ")
            date_str = input("Date (YYYY-MM-DD): ")
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            type = input("Type: ")
            complaint = Complaint(code, complainant, accused, date, type)
            complaint_list.add(complaint)
        elif option == "2":
            code = int(input("Code of the complaint to remove: "))
            if complaint_list.remove(code):
                print("Complaint removed successfully.")
            else:
                print("Complaint not found.")
        elif option == "3":
            name = input("Name of the person: ")
            sublist = complaint_list.complaints_by_person(name)
            for complaint in sublist:
                print(complaint)
        elif option == "4":
            type = input("Type of complaint: ")
            percentage = complaint_list.percentage_by_type(type)
            print(f"Percentage of '{type}' complaints: {percentage:.2f}%")
        elif option == "5":
            complaint_list.show_complaints()
        elif option == "6":
            code = int(input("Code of the complaint: "))
            new_date_str = input("New date (YYYY-MM-DD): ")
            new_date = datetime.strptime(new_date_str, "%Y-%m-%d").date()
            if complaint_list.set_date(code, new_date):
                print("Date modified successfully.")
            else:
                print("Complaint not found.")
        elif option == "7":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
