import csv

class HolidayExpenseTracker:
    def __init__(self):
        self.expenses = []

    # Add a new expense to the tracker.
    def add_expense(self, amount, description):
        self.expenses.append({'amount': amount, 'description': description})
        print(f"Added expense: {description} - ${amount:.2f}")

    # Edit an existing expense.
    def edit_expense(self, index, new_amount, new_description):
        if 0 <= index < len(self.expenses):
            self.expenses[index] = {'amount': new_amount, 'description': new_description}
            print(f"Edited expense at index {index}: {new_description} - ${new_amount:.2f}")
        else:
            print("Invalid index. Please try again.")

    # Delete an expense from the tracker.
    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            removed = self.expenses.pop(index)
            print(f"Deleted expense: {removed['description']} - ${removed['amount']:.2f}")
        else:
            print("Invalid index. Please try again.")

    # Calculate the total of all expenses.
    def calculate_total(self):
        return sum(expense['amount'] for expense in self.expenses)

    # Calculate the average of all expenses.
    def calculate_average(self):
        if not self.expenses:
            return 0
        return self.calculate_total() / len(self.expenses)

    # Find the highest expense.
    def find_highest_expense(self):
        if not self.expenses:
            return None
        return max(self.expenses, key=lambda x: x['amount'])

    # Save expenses to a CSV file.
    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Description', 'Amount'])
            for expense in self.expenses:
                writer.writerow([expense['description'], expense['amount']])
        print(f"Expenses saved to {filename}")

    # Load expenses from a CSV file.
    def load_from_csv(self, filename):
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                self.expenses = [{'description': row['Description'], 'amount': float(row['Amount'])} for row in reader]
            print(f"Expenses loaded from {filename}")
        except FileNotFoundError:
            print(f"The file {filename} does not exist.")
        except Exception as e:
            print(f"An error occurred while loading from CSV: {e}")

def main():
    tracker = HolidayExpenseTracker()
    
    while True:
        print("\nHoliday Expense Tracker")
        print("1. Add Expense")
        print("2. Edit Expense")
        print("3. Delete Expense")
        print("4. View Total Expenses")
        print("5. View Average Expense")
        print("6. View Highest Expense")
        print("7. Save Expenses to CSV")
        print("8. Load Expenses from CSV")
        print("9. Exit")

        choice = input("Choose an option (1-9): ")

        if choice == '1':
            amount = float(input("Enter the amount: "))
            description = input("Enter the description: ")
            tracker.add_expense(amount, description)
        
        elif choice == '2':
            index = int(input("Enter the index of the expense to edit: ")) - 1
            new_amount = float(input("Enter the new amount: "))
            new_description = input("Enter the new description: ")
            tracker.edit_expense(index, new_amount, new_description)
        
        elif choice == '3':
            index = int(input("Enter the index of the expense to delete: ")) - 1
            tracker.delete_expense(index)
        
        elif choice == '4':
            total = tracker.calculate_total()
            print(f"Total Expenses: ${total:.2f}")
        
        elif choice == '5':
            average = tracker.calculate_average()
            print(f"Average Expense: ${average:.2f}")
        
        elif choice == '6':
            highest_expense = tracker.find_highest_expense()
            if highest_expense:
                print(f"Highest Expense: {highest_expense['description']} - ${highest_expense['amount']:.2f}")
            else:
                print("No expenses recorded.")
        
        elif choice == '7':
            filename = input("Enter filename to save (e.g., expenses.csv): ")
            tracker.save_to_csv(filename)
        
        elif choice == '8':
            filename = input("Enter filename to load (e.g., expenses.csv): ")
            tracker.load_from_csv(filename)
        
        elif choice == '9':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
