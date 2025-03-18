# Import necessary libraries
import matplotlib.pyplot as plt

# Handles all user interactions and displays.
class View:
    # Display the main menu.
    @staticmethod
    def display_menu():
        print("\n Banking System Menu by David Caleb")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. View Transaction History")
        print("6. Apply Interest (Savings Account)")
        print("7. Transfer Funds")
        print("8. Delete Account")
        print("9. View Account Summary")
        print("10. Visualize Account Balances")
        print("11. Visualize Transaction History")
        print("12. Exit")

    # Get input from the user.
    @staticmethod
    def get_user_input(prompt):
        return input(prompt)

    # Display a message to the user.
    @staticmethod
    def display_message(message):
        print(message)

    # Display account details.
    @staticmethod
    def display_account_details(account):
        if account:
            print(f"Account Number: {account.account_number}, Customer Name: {account.customer_name}, Balance: {account.get_balance()}")
        else:
            print("Account not found.")

    # Display transaction history.
    @staticmethod
    def display_transaction_history(transactions):
        if transactions:
            for transaction in transactions:
                print(f"{transaction.transaction_type}: ${transaction.amount}")
        else:
            print("No transactions found.")

    # Plot transaction history using matplotlib.
    @staticmethod
    def plot_transaction_history(transactions):
        if transactions:
            types = [t.transaction_type for t in transactions]
            amounts = [t.amount for t in transactions]
            plt.bar(types, amounts, color=['green' if t == 'Deposit' else 'red' for t in types])
            plt.title("Transaction History")
            plt.xlabel("Transaction Type")
            plt.ylabel("Amount ($)")
            plt.show()
        else:
            print("No transactions to display.")

    # Plot account balances using matplotlib.
    @staticmethod
    def plot_account_balances(accounts):
        balances = [account.get_balance() for account in accounts]
        labels = [f"{account.customer_name}\nAcc#{account.account_number}" for account in accounts]
        plt.pie(balances, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title("Account Balances Distribution")
        plt.show()

    # Plot balance trend over time using matplotlib.
    @staticmethod
    def plot_balance_trend(account):
        if account:
            balances = []
            balance = 0
            for transaction in account.get_transaction_history():
                if transaction.transaction_type == "Deposit":
                    balance += transaction.amount
                else:
                    balance -= transaction.amount
                balances.append(balance)
            plt.plot(balances, marker='o')
            plt.title("Balance Trend Over Time")
            plt.xlabel("Transaction Number")
            plt.ylabel("Balance ($)")
            plt.show()
        else:
            print("No account found.")