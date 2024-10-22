# Importing necessary libraries
import tkinter as tk
from tkinter import messagebox

# Function to calculate the tip and total amount
def calculate_tip():
    try:
        # Get the total bill amount and tip percentage entered by the user
        bill_amount = float(entry_bill.get())
        tip_percentage = float(entry_tip.get())
        
        # Calculate the tip amount
        tip_amount = (tip_percentage / 100) * bill_amount
        
        # Calculate the total amount (bill + tip)
        total_amount = bill_amount + tip_amount
        
        # Display the results
        label_tip_result.config(text=f"Tip Amount: ${tip_amount:.2f}")
        label_total_result.config(text=f"Total Amount: ${total_amount:.2f}")
    
    except ValueError:
        # Handle the case when input is not a valid number
        messagebox.showerror("Input Error", "Please enter valid numbers for bill and tip percentage.")

# Create the main window
root = tk.Tk()
root.title("Tip Calculator by David Caleb")
root.configure(bg="#2E2E2E")
root.geometry('400x400')

# Create and position widgets
label_bill = tk.Label(root, text="Enter Bill Amount ($):", font=("Trebuchet MS", 12))
label_bill.pack(pady=10)
entry_bill = tk.Entry(root, font=("Trebuchet MS", 12))
entry_bill.pack(pady=5)

label_tip = tk.Label(root, text="Enter Tip Percentage (%):", font=("Trebuchet MS", 12))
label_tip.pack(pady=10)
entry_tip = tk.Entry(root, font=("Trebuchet MS", 12))
entry_tip.pack(pady=5)

# Button to calculate the tip and total
button_calculate = tk.Button(root, text="Calculate Tip", command=calculate_tip, font=("Trebuchet MS", 12))
button_calculate.pack(pady=20)

# Labels to display the calculated tip and total amount
label_tip_result = tk.Label(root, text="Tip Amount: $0.00", font=("Trebuchet MS", 12))
label_tip_result.pack(pady=5)
label_total_result = tk.Label(root, text="Total Amount: $0.00", font=("Trebuchet MS", 12))
label_total_result.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
