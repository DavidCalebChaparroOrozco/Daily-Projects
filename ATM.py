# Importing necessary libraries
import tkinter as tk
from tkinter import messagebox

# Initializing the main application window
class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Machine by David Caleb")
        self.root.geometry("400x400")
        self.root.resizable(False, False)  
        self.root.configure(bg="gray20")

        # User account details
        self.balance = 1000  # Initial balance
        self.pin = "1234"    # User PIN

        self.create_widgets()

    def create_widgets(self):
        # Create a frame to hold the PIN entry section
        self.pin_frame = tk.Frame(self.root, bg="gray20")  # Set the frame background color
        self.pin_frame.pack(pady=20)

        self.label = tk.Label(self.pin_frame, text="Welcome to the ATM", font=("Helvetica", 16), fg="white", bg="gray20")  # Set text and background colors
        self.label.pack()

        # PIN entry section
        self.pin_label = tk.Label(self.pin_frame, text="Enter PIN:", fg="white", bg="gray20")  # Set text color
        self.pin_label.pack(pady=5)

        self.pin_entry = tk.Entry(self.pin_frame, show="*", font=("Helvetica", 12), validate="key", validatecommand=(self.root.register(self.validate_numeric), "%S"))
        self.pin_entry.pack(pady=5)

        self.pin_button = tk.Button(self.pin_frame, text="Submit", command=self.check_pin, font=("Helvetica", 12), bg="gray40", fg="white")  # Set button colors
        self.pin_button.pack(pady=10)

    def validate_numeric(self, char):
        # Validate if the input is a numeric character
        return char.isdigit()

    def check_pin(self):
        entered_pin = self.pin_entry.get()
        if entered_pin == self.pin:
            self.show_menu()
        else:
            messagebox.showerror("Error", "Incorrect PIN")

    def show_menu(self):
        # Clear previous widgets
        self.clear_screen()

        # Create a frame to hold the menu buttons
        self.menu_frame = tk.Frame(self.root, bg="gray20")
        self.menu_frame.pack(pady=20)

        self.menu_label = tk.Label(self.menu_frame, text="ATM Menu", font=("Helvetica", 16), fg="white", bg="gray20")
        self.menu_label.pack()

        self.balance_button = tk.Button(self.menu_frame, text="Check Balance", command=self.check_balance, font=("Helvetica", 12), bg="gray40", fg="white")
        self.balance_button.pack(pady=10)

        self.deposit_button = tk.Button(self.menu_frame, text="Deposit Money", command=self.deposit_money, font=("Helvetica", 12), bg="gray40", fg="white")
        self.deposit_button.pack(pady=10)

        self.withdraw_button = tk.Button(self.menu_frame, text="Withdraw Money", command=self.withdraw_money, font=("Helvetica", 12), bg="gray40", fg="white")
        self.withdraw_button.pack(pady=10)

        self.exit_button = tk.Button(self.menu_frame, text="Exit", command=self.root.quit, font=("Helvetica", 12), bg="gray40", fg="white")
        self.exit_button.pack(pady=10)

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is: ${self.balance}")

    def deposit_money(self):
        self.clear_screen()

        # Create a frame to hold the deposit section
        self.deposit_frame = tk.Frame(self.root, bg="gray20")
        self.deposit_frame.pack(pady=20)

        self.deposit_label = tk.Label(self.deposit_frame, text="Enter amount to deposit:", fg="white", bg="gray20")
        self.deposit_label.pack(pady=5)

        self.deposit_entry = tk.Entry(self.deposit_frame, font=("Helvetica", 12), validate="key", validatecommand=(self.root.register(self.validate_numeric), "%S"))
        self.deposit_entry.pack(pady=5)

        self.deposit_button = tk.Button(self.deposit_frame, text="Deposit", command=self.process_deposit, font=("Helvetica", 12), bg="gray40", fg="white")
        self.deposit_button.pack(pady=10)

    def process_deposit(self):
        try:
            amount = float(self.deposit_entry.get())
            if amount <= 0:
                raise ValueError("Amount must be positive")
            self.balance += amount
            messagebox.showinfo("Success", f"${amount} deposited successfully.")
            self.show_menu()
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

    def withdraw_money(self):
        self.clear_screen()

        # Create a frame to hold the withdraw section
        self.withdraw_frame = tk.Frame(self.root, bg="gray20")
        self.withdraw_frame.pack(pady=20)

        self.withdraw_label = tk.Label(self.withdraw_frame, text="Enter amount to withdraw:", fg="white", bg="gray20")
        self.withdraw_label.pack(pady=5)

        self.withdraw_entry = tk.Entry(self.withdraw_frame, font=("Helvetica", 12), validate="key", validatecommand=(self.root.register(self.validate_numeric), "%S"))
        self.withdraw_entry.pack(pady=5)

        self.withdraw_button = tk.Button(self.withdraw_frame, text="Withdraw", command=self.process_withdraw, font=("Helvetica", 12), bg="gray40", fg="white")
        self.withdraw_button.pack(pady=10)

    def process_withdraw(self):
        try:
            amount = float(self.withdraw_entry.get())
            if amount <= 0:
                raise ValueError("Amount must be positive")
            if amount > self.balance:
                messagebox.showerror("Error", "Insufficient balance")
            else:
                self.balance -= amount
                messagebox.showinfo("Success", f"${amount} withdrawn successfully.")
            self.show_menu()
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

    def clear_screen(self):
        # Remove all widgets from the screen
        for widget in self.root.winfo_children():
            widget.pack_forget()

# Main loop to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()