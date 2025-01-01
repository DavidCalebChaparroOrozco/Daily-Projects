# Importing necessary libraries
import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
import csv
import pandas as pd

# Class to manage the budget planner application
class BudgetPlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Family Budget Planner by David Caleb")
        self.root.geometry('500x550')
        self.root.configure(bg="#2E2E2E")

        # Initialize expenses list and budget
        self.expenses = []
        self.budget_limit = 0

        # Create and place widgets for expenses input
        label_style = {'bg': '#2E2E2E', 'fg': '#FFFFFF'}
        entry_style = {'bg': '#4E4E4E', 'fg': '#FFFFFF', 'insertbackground': 'white'}

        tk.Label(root, text="Food Expenses ($):", **label_style).pack(pady=5)
        self.food_entry = tk.Entry(root, **entry_style)
        self.food_entry.pack(pady=5)

        tk.Label(root, text="Gifts Expenses ($):", **label_style).pack(pady=5)
        self.gifts_entry = tk.Entry(root, **entry_style)
        self.gifts_entry.pack(pady=5)

        tk.Label(root, text="Entertainment Expenses ($):", **label_style).pack(pady=5)
        self.entertainment_entry = tk.Entry(root, **entry_style)
        self.entertainment_entry.pack(pady=5)

        tk.Label(root, text="Monthly Budget Limit ($):", **label_style).pack(pady=5)
        self.budget_entry = tk.Entry(root, **entry_style)
        self.budget_entry.pack(pady=5)

        # Create buttons for actions
        calculate_button = tk.Button(root, text="Add Expenses", command=self.add_expenses, bg="#007BFF", fg="#FFFFFF")
        calculate_button.pack(pady=10)

        view_history_button = tk.Button(root, text="View Expense History", command=self.view_history, bg="#28A745", fg="#FFFFFF")
        view_history_button.pack(pady=10)

        export_button = tk.Button(root, text="Export to CSV", command=self.export_to_csv, bg="#FFC107", fg="#FFFFFF")
        export_button.pack(pady=10)

        plot_button = tk.Button(root, text="Plot Expenses", command=self.plot_expenses, bg="#17A2B8", fg="#FFFFFF")
        plot_button.pack(pady=10)

        clear_button = tk.Button(root, text="Clear All Data", command=self.clear_all_data, bg="#DC3545", fg="#FFFFFF")
        clear_button.pack(pady=10)

        import_button = tk.Button(root, text="Import from Excel/CSV", command=self.import_from_file, bg="#6F42C1", fg="#FFFFFF")
        import_button.pack(pady=10)

    # Function to add expenses and validate inputs
    def add_expenses(self):
        try:
            food_expense = float(self.food_entry.get())
            gifts_expense = float(self.gifts_entry.get())
            entertainment_expense = float(self.entertainment_entry.get())
            monthly_budget = float(self.budget_entry.get())

            # Validate inputs
            if food_expense < 0 or gifts_expense < 0 or entertainment_expense < 0 or monthly_budget < 0:
                raise ValueError("Expenses and budget must be non-negative.")

            total_expenses = food_expense + gifts_expense + entertainment_expense
            
            # Store expenses in a list
            self.expenses.append({
                "Food": food_expense,
                "Gifts": gifts_expense,
                "Entertainment": entertainment_expense,
                "Total": total_expenses,
                "Budget": monthly_budget,
            })

            # Alert user about total expenses and budget status
            if total_expenses > monthly_budget:
                messagebox.showwarning("Budget Alert", f"You have exceeded your budget by ${total_expenses - monthly_budget:.2f}.")
            else:
                messagebox.showinfo("Expenses Added", f"Total expenses added: ${total_expenses:.2f}")

            # Clear entries after adding expenses
            self.clear_entries()

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    # Function to clear all data and reset the application
    def clear_all_data(self):
        self.expenses.clear()  
        self.clear_entries() 
        messagebox.showinfo("Data Cleared", "All data has been cleared.")

    # Function to convert CSV to XLSX if necessary and import expenses from a file
    def import_from_file(self):
        try:
            file_path = 'expenses.csv'
            
            # Convert CSV to XLSX if it exists
            if file_path.endswith('.csv'):
                xlsx_path = file_path.replace('.csv', '.xlsx')
                self.convert_csv_to_xlsx(file_path, xlsx_path)

            data = pd.read_excel(xlsx_path)  # Read the Excel file

            for index, row in data.iterrows():
                food_expense = row['Food']
                gifts_expense = row['Gifts']
                entertainment_expense = row['Entertainment']
                monthly_budget = row['Budget']

                if food_expense < 0 or gifts_expense < 0 or entertainment_expense < 0 or monthly_budget < 0:
                    continue

                total_expenses = food_expense + gifts_expense + entertainment_expense
                
                # Store expenses in a list
                self.expenses.append({
                    "Food": food_expense,
                    "Gifts": gifts_expense,
                    "Entertainment": entertainment_expense,
                    "Total": total_expenses,
                    "Budget": monthly_budget,
                })

            messagebox.showinfo("Import Successful", f"Imported {len(data)} entries from Excel.")
        
        except Exception as e:
            messagebox.showerror("Import Error", str(e))

    # Function to convert CSV to XLSX format using pandas
    def convert_csv_to_xlsx(self, csv_file_path, xlsx_file_path):
        try:
            data = pd.read_csv(csv_file_path)
            data.to_excel(xlsx_file_path, index=False)
            messagebox.showinfo("Conversion Successful", f"Converted {csv_file_path} to {xlsx_file_path}.")
        
        except Exception as e:
            messagebox.showerror("Conversion Error", str(e))

    # Function to view expense history in a new window
    def view_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("Expense History")
        
        history_text = tk.Text(history_window, width=60, height=15)
        
        for expense in self.expenses:
            history_text.insert(tk.END, f"Food: ${expense['Food']}, Gifts: ${expense['Gifts']}, "
                                        f"Entertainment: ${expense['Entertainment']}, "
                                        f"Total: ${expense['Total']}, Budget: ${expense['Budget']}\n")

        history_text.pack()
    
    # Function to export expenses to CSV file
    def export_to_csv(self):
        with open('expenses.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Food", "Gifts", "Entertainment", "Total", "Budget"])
            for expense in self.expenses:
                writer.writerow([expense['Food'], expense['Gifts'], expense['Entertainment'],
                                expense['Total'], expense['Budget']])
        
        messagebox.showinfo("Export Successful", "Expenses exported to expenses.csv")

    # Function to plot expenses using matplotlib
    def plot_expenses(self):
        if not self.expenses:
            messagebox.showwarning("No Data", "No expenses to plot.")
            return
        
        categories = ['Food', 'Gifts', 'Entertainment']
        values = [sum(expense[category] for expense in self.expenses) for category in categories]

        if sum(values) == 0:
            messagebox.showinfo("No Data", "All expense categories have zero value.")
            return

        plt.style.use('ggplot')

        plt.figure(figsize=(6, 6))  
        plt.pie(
            values,
            labels=categories,
            autopct='%1.1f%%',
            startangle=140,
            wedgeprops={'edgecolor': 'white'}
        )
        
        plt.title('Distribution of Expenses', fontsize=16)
        
        plt.show()

    # Function to clear input fields after adding expenses
    def clear_entries(self):
        self.food_entry.delete(0, tk.END)
        self.gifts_entry.delete(0, tk.END)
        self.entertainment_entry.delete(0, tk.END)
        self.budget_entry.delete(0, tk.END)

# Main execution of the application
if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetPlanner(root)
    root.mainloop()
