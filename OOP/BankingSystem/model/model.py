# Represents a bank account with basic operations like deposit and withdraw.
class Account:
    def __init__(self, account_number, customer_name, balance=0):
        # Encapsulated account number
        self.account_number = account_number  
        # Customer name associated with the account
        self.customer_name = customer_name  
        # Encapsulated balance
        self.balance = balance  
        # List to store transaction history
        self.transactions = []  

    # Deposit money into the account.
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction("Deposit", amount))
            return True
        return False

    # Withdraw money from the account.
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction("Withdraw", amount))
            return True
        return False

    # Get the current balance.
    def get_balance(self):
        return self.balance

    # Get the transaction history.
    def get_transaction_history(self):
        return self.transactions


# A savings account with an interest rate.
class SavingsAccount(Account):
    def __init__(self, account_number, customer_name, balance=0, interest_rate=0.01):
        super().__init__(account_number, customer_name, balance)
        self.interest_rate = interest_rate

    # Apply interest to the account balance.
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        return interest


# A checking account with no interest.
class CheckingAccount(Account):
    def __init__(self, account_number, customer_name, balance=0):
        super().__init__(account_number, customer_name, balance)


# Represents a transaction with details like type and amount.
class Transaction:
    def __init__(self, transaction_type, amount):
        # e.g., "Deposit" or "Withdraw"
        self.transaction_type = transaction_type  
        self.amount = amount


# Represents a bank with a collection of accounts.
class Bank:
    def __init__(self, name):
        self.name = name
        # Dictionary to store accounts (key: account_number, value: Account)
        self.accounts = {}  

    # Add an account to the bank.
    def add_account(self, account):
        self.accounts[account.account_number] = account

    # Retrieve an account by its number.
    def get_account(self, account_number):
        return self.accounts.get(account_number)

    # Delete an account by its number.
    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            return True
        return False

    # Transfer funds between two accounts.
    def transfer_funds(self, from_account_number, to_account_number, amount):
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)
        if from_account and to_account and from_account.withdraw(amount):
            to_account.deposit(amount)
            return True
        return False

    # Get a list of all accounts.
    def get_all_accounts(self):
        return list(self.accounts.values())