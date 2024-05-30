# The “Su Ahorrito” bank requires that you design a system that allows you to manage user attention.
# It is known that for each user there is the id, the name and the generated turn. 
# On the other hand, the bank manages three types of clients, 
# one general user and two preferential users.
# Create a system that allows:
#   Assign a shift to the client.
#   Serve a customer and handle the cashier. When a customer is served, the service receipt is stored in a stack.
#   Determine the % of each type of transaction (consignment, withdrawal, bill payment)
#   Delete a shift.
#   Determine the number of shifts a client has, additionally leave them in the one with the most shifts.
#   Show the information of the transactions carried out

# Import necessary libraries
from collections import deque
from enum import Enum
import random

class ClientType(Enum):
    # Define the types of clients
    GENERAL = 1
    PREFERENTIAL1 = 2
    PREFERENTIAL2 = 3

class Transaction(Enum):
    # Define the types of transactions
    DEPOSIT = 1
    WITHDRAWAL = 2
    BILL_PAYMENT = 3

class User:
    def __init__(self, user_id, name, client_type):
        # Initialize user with id, name, and client type
        self.user_id = user_id
        self.name = name
        self.client_type = client_type
        self.turns = deque()

    def assign_turn(self, turn):
        # Assign a turn to the user
        self.turns.append(turn)

    def remove_turn(self):
        # Remove a turn from the user
        if self.turns:
            self.turns.popleft()

    def turn_count(self):
        # Get the number of turns the user has
        return len(self.turns)

class Turn:
    def __init__(self, turn_id, user, transaction):
        # Initialize turn with id, user, and transaction type
        self.turn_id = turn_id
        self.user = user
        self.transaction = transaction

class Bank:
    def __init__(self):
        # Initialize bank with turns, receipts, and users
        self.turns = deque()
        self.receipts = []
        self.users = []

    def add_user(self, user):
        # Add a user to the bank
        self.users.append(user)

    def assign_turn(self, user):
        # Assign a turn to a user and add it to the queue
        turn_id = len(self.turns) + 1
        transaction = random.choice(list(Transaction))
        turn = Turn(turn_id, user, transaction)
        user.assign_turn(turn)
        self.turns.append(turn)
        print(f"Turn {turn_id} assigned to user {user.name} for {transaction.name}.")

    def attend_client(self):
        # Attend the next client in the queue and store the receipt
        if self.turns:
            turn = self.turns.popleft()
            self.receipts.append(turn)
            turn.user.remove_turn()
            print(f"Client {turn.user.name} attended for {turn.transaction.name}. Turn ID: {turn.turn_id}")
        else:
            print("No clients to attend.")

    def transaction_percentage(self):
        # Calculate the percentage of each type of transaction
        total_transactions = len(self.receipts)
        if total_transactions == 0:
            return {t: 0 for t in Transaction}
        transaction_count = {t: 0 for t in Transaction}
        for receipt in self.receipts:
            transaction_count[receipt.transaction] += 1
        return {t: (count / total_transactions) * 100 for t, count in transaction_count.items()}

    def remove_turn(self, turn_id):
        # Remove a specific turn from the queue
        self.turns = deque(turn for turn in self.turns if turn.turn_id != turn_id)
        print(f"Turn {turn_id} removed.")

    def client_turn_count(self, user):
        # Get the number of turns a user has
        return user.turn_count()

    def show_completed_transactions(self):
        # Show all completed transactions
        if not self.receipts:
            print("No transactions completed.")
        for receipt in self.receipts:
            print(f"Turn ID: {receipt.turn_id}, User: {receipt.user.name}, Transaction: {receipt.transaction.name}")

def menu():
    bank = Bank()

    while True:
        print("\nBank Management System")
        print("1. Create user")
        print("2. Add user to bank")
        print("3. Assign turn to user")
        print("4. Attend client")
        print("5. Show transaction percentages")
        print("6. Remove a turn")
        print("7. Show user turn count")
        print("8. Show completed transactions")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Create a new user
            user_id = int(input("Enter user ID: "))
            name = input("Enter user name: ")
            print("Select client type:")
            print("1. General")
            print("2. Preferential 1")
            print("3. Preferential 2")
            client_type_choice = int(input("Enter client type (1-3): "))
            if client_type_choice == 1:
                client_type = ClientType.GENERAL
            elif client_type_choice == 2:
                client_type = ClientType.PREFERENTIAL1
            elif client_type_choice == 3:
                client_type = ClientType.PREFERENTIAL2
            user = User(user_id, name, client_type)
            print(f"User {name} created successfully.")

        elif choice == "2":
            # Add the created user to the bank
            bank.add_user(user)
            print(f"User {user.name} added to the bank.")

        elif choice == "3":
            # Assign a turn to an existing user
            user_id = int(input("Enter user ID to assign turn: "))
            user = next((u for u in bank.users if u.user_id == user_id), None)
            if user:
                bank.assign_turn(user)
            else:
                print("User not found.")

        elif choice == "4":
            # Attend the next client in the queue
            bank.attend_client()

        elif choice == "5":
            # Show the percentages of each type of transaction
            percentages = bank.transaction_percentage()
            print("Transaction percentages:")
            for transaction, percentage in percentages.items():
                print(f"{transaction.name}: {percentage:.2f}%")

        elif choice == "6":
            # Remove a specific turn from the queue
            turn_id = int(input("Enter turn ID to remove: "))
            bank.remove_turn(turn_id)

        elif choice == "7":
            # Show the number of turns a specific user has
            user_id = int(input("Enter user ID to show turn count: "))
            user = next((u for u in bank.users if u.user_id == user_id), None)
            if user:
                turn_count = bank.client_turn_count(user)
                print(f"User {user.name} has {turn_count} turns.")
            else:
                print("User not found.")

        elif choice == "8":
            # Show all completed transactions
            print("Completed transactions:")
            bank.show_completed_transactions()

        elif choice == "9":
            # Exit the menu
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the menu
menu()
