from controller.controller import Controller
from model.model import Bank
from view.view import View

def main():
    bank = Bank("MyBank")
    controller = Controller(bank)
    view = View()

    while True:
        view.display_menu()
        choice = view.get_user_input("Enter your choice: ")

        # Create Account
        if choice == "1":  
            account_number = view.get_user_input("Enter account number: ")
            customer_name = view.get_user_input("Enter customer name: ")
            account_type = view.get_user_input("Enter account type (savings/checking): ").lower()
            initial_balance = float(view.get_user_input("Enter initial balance: "))
            if controller.create_account(account_number, customer_name, account_type, initial_balance):
                view.display_message("Account created successfully.")
            else:
                view.display_message("Account creation failed. Account number already exists.")

        # Deposit
        elif choice == "2":  
            account_number = view.get_user_input("Enter account number: ")
            amount = float(view.get_user_input("Enter amount to deposit: "))
            if controller.deposit(account_number, amount):
                view.display_message("Deposit successful.")
            else:
                view.display_message("Deposit failed. Check account number.")

        # Withdraw
        elif choice == "3":  
            account_number = view.get_user_input("Enter account number: ")
            amount = float(view.get_user_input("Enter amount to withdraw: "))
            if controller.withdraw(account_number, amount):
                view.display_message("Withdrawal successful.")
            else:
                view.display_message("Withdrawal failed. Check account number or balance.")

        # Check Balance
        elif choice == "4":  
            account_number = view.get_user_input("Enter account number: ")
            account = controller.check_balance(account_number)
            view.display_account_details(account)

        # View Transaction History
        elif choice == "5":  
            account_number = view.get_user_input("Enter account number: ")
            transactions = controller.get_transaction_history(account_number)
            view.display_transaction_history(transactions)
            view.plot_transaction_history(transactions)

        # Apply Interest
        elif choice == "6":  
            account_number = view.get_user_input("Enter account number: ")
            interest = controller.apply_interest(account_number)
            if interest is not None:
                view.display_message(f"Interest applied: ${interest:.2f}")
            else:
                view.display_message("Interest application failed. Check account type.")

        # Transfer Funds
        elif choice == "7":  
            from_account = view.get_user_input("Enter source account number: ")
            to_account = view.get_user_input("Enter destination account number: ")
            amount = float(view.get_user_input("Enter amount to transfer: "))
            if controller.transfer_funds(from_account, to_account, amount):
                view.display_message("Transfer successful.")
            else:
                view.display_message("Transfer failed. Check account numbers or balance.")

        # Delete Account
        elif choice == "8":  
            account_number = view.get_user_input("Enter account number: ")
            if controller.delete_account(account_number):
                view.display_message("Account deleted successfully.")
            else:
                view.display_message("Account deletion failed. Check account number.")

        # View Account Summary
        elif choice == "9":  
            accounts = controller.get_all_accounts()
            for account in accounts:
                view.display_account_details(account)

        # Visualize Account Balances
        elif choice == "10":  
            accounts = controller.get_all_accounts()
            view.plot_account_balances(accounts)

        # Visualize Transaction History
        elif choice == "11":  
            account_number = view.get_user_input("Enter account number: ")
            account = controller.check_balance(account_number)
            view.plot_balance_trend(account)

        # Exit
        elif choice == "12":  
            view.display_message("Thank you for using the Banking System. Goodbye!")
            break

        else:
            view.display_message("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()