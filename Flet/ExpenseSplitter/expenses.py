class Expense:
    def __init__(self, description, amount, participants):
        self.description = description
        self.amount = amount
        self.participants = participants

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount, participants):
        expense = Expense(description, amount, participants)
        self.expenses.append(expense)

    def calculate_owed(self):
        total_per_person = {}
        for expense in self.expenses:
            share = expense.amount / len(expense.participants)
            for participant in expense.participants:
                if participant not in total_per_person:
                    total_per_person[participant] = 0
                total_per_person[participant] += share
        return total_per_person

    def get_expenses(self):
        return self.expenses
