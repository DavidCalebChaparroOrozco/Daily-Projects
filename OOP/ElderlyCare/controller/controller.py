from model.model import ElderlyCareModel
from view.view import ElderlyCareView

# Manages the interaction between the model and the view.
class ElderlyCareController:
    
    def __init__(self):
        self.model = ElderlyCareModel()
        self.view = ElderlyCareView()

    # Runs the ElderlyCare system.
    def run(self):
        while True:
            self.view.display_menu()
            choice = self.view.get_user_input("Enter your choice: ")

            if choice == "1":
                self.add_elderly_person()
            elif choice == "2":
                self.view_all_elderly_persons()
            elif choice == "3":
                self.add_medication_record()
            elif choice == "4":
                self.view_medication_history()
            elif choice == "5":
                self.view.display_message("Exiting the system. Goodbye!")
                break
            else:
                self.view.display_message("Invalid choice. Please try again.")

    # Adds a new elderly person to the system.
    def add_elderly_person(self):
        name = self.view.get_user_input("Enter name: ")
        age = self.view.get_user_input("Enter age: ")
        health_condition = self.view.get_user_input("Enter health condition: ")
        self.model.add_elderly_person(name, age, health_condition)
        self.view.display_message("Elderly person added successfully.")

    # Displays all elderly persons in the system.
    def view_all_elderly_persons(self):
        persons = self.model.get_all_elderly_persons()
        self.view.display_elderly_persons(persons)

    # Adds a medication record to an elderly person.
    def add_medication_record(self):
        name = self.view.get_user_input("Enter the name of the elderly person: ")
        person = self.model.get_elderly_person_by_name(name)
        if person:
            medication_name = self.view.get_user_input("Enter medication name: ")
            dosage = self.view.get_user_input("Enter dosage: ")
            date = self.view.get_user_input("Enter date (YYYY-MM-DD): ")
            person.add_medication(medication_name, dosage, date)
            self.view.display_message("Medication record added successfully.")
        else:
            self.view.display_message("Elderly person not found.")

    # Displays the medication history of an elderly person.
    def view_medication_history(self):
        name = self.view.get_user_input("Enter the name of the elderly person: ")
        person = self.model.get_elderly_person_by_name(name)
        if person:
            history = person.get_medication_history()
            self.view.display_medication_history(history)
        else:
            self.view.display_message("Elderly person not found.")