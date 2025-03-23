# Handles the display of information to the user.
class ElderlyCareView:
    
    @staticmethod
    # Displays the main menu to the user.
    def display_menu():
        print(" ElderlyCare System ".center(50, "="))
        print("1. Add Elderly Person")
        print("2. View All Elderly Persons")
        print("3. Add Medication Record")
        print("4. View Medication History")
        print("5. Exit")

    @staticmethod
    # Gets input from the user.
    def get_user_input(prompt):
        return input(prompt)

    @staticmethod
    # Displays a message to the user.
    def display_message(message):
        print(message)

    @staticmethod
    # Displays a list of elderly persons.
    def display_elderly_persons(persons):
        if not persons:
            print("No elderly persons found.")
        else:
            for person in persons:
                print(person)

    @staticmethod
    # Displays the medication history of an elderly person.
    def display_medication_history(history):
        if not history:
            print("No medication history found.")
        else:
            for record in history:
                print(f"Medication: {record['medication_name']}, Dosage: {record['dosage']}, Date: {record['date']}")