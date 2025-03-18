from model.model import Account, SavingsAccount, CheckingAccount, Bank

# Handles the logic between the view and the model.
class Controller:
    def __init__(self, bank):
        self.bank = bank

    # Create a new account.
    def create_account(self, account_number, customer_name, account_type, initial_balance=0):
        if account_number in self.bank.accounts:
            return False
        if account_type == "savings":
            account = SavingsAccount(account_number, customer_name, initial_balance)
        else:
            account = CheckingAccount(account_number, customer_name, initial_balance)
        self.bank.add_account(account)
        return True

    # Deposit money into an account.
    def deposit(self, account_number, amount):
        account = self.bank.get_account(account_number)
        if account and account.deposit(amount):
            return True
        return False

    # Withdraw money from an account.
    def withdraw(self, account_number, amount):
        account = self.bank.get_account(account_number)
        if account and account.withdraw(amount):
            return True
        return False

    # Check the balance of an account.
    def check_balance(self, account_number):
        return self.bank.get_account(account_number)

    # Get transaction history for an account.
    def get_transaction_history(self, account_number):
        account = self.bank.get_account(account_number)
        if account:
            return account.get_transaction_history()
        return None

    # Apply interest to a savings account.
    def apply_interest(self, account_number):
        account = self.bank.get_account(account_number)
        if isinstance(account, SavingsAccount):
            return account.apply_interest()
        return None

    # Transfer funds between two accounts.
    def transfer_funds(self, from_account_number, to_account_number, amount):
        return self.bank.transfer_funds(from_account_number, to_account_number, amount)

    # Delete an account.
    def delete_account(self, account_number):
        return self.bank.delete_account(account_number)

    # Get a list of all accounts.
    def get_all_accounts(self):
        return self.bank.get_all_accounts()