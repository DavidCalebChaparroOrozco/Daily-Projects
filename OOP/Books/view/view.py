# View class to handle user interface
class View:
    @staticmethod
    def display_menu():
        print("\nBook Subscription System")
        print("1. Subscribe to a genre")
        print("2. Display reader details")
        print("3. Display book details")
        print("4. Exit")
        print("=".center(50, "="))
        return input("Select an option: ")

    @staticmethod
    def show_message(message):
        print(message)

    @staticmethod
    def get_input(prompt):
        return input(prompt)
