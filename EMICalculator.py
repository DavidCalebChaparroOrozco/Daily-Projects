# Importing necessary libraries
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Calculates the Equated Monthly Installment (EMI) based on user input.
def calculate_emi():
    try:
        # Retrieve and convert user inputs for total amount, years, months, and interest rate.
        total = float(total_entry.get())
        years = int(years_var.get())
        months = int(months_var.get())
        interest_rate = float(interest_entry.get())

        # Calculate total number of months and monthly interest rate.
        total_months = years * 12 + months
        monthly_interest_rate = interest_rate / (12 * 100)

        # Calculate the EMI using the formula.
        emi = (total * monthly_interest_rate * (1 + monthly_interest_rate) ** total_months) / \
              ((1 + monthly_interest_rate) ** total_months - 1)
        
        # Calculate total payment and interest amount.
        total_payment = emi * total_months
        interest_amount = total_payment - total

        # Format and display the results in a message box.
        result_text = f"""
        Monthly payment: {emi:,.2f}
        EMI Period: {total_months} Months
        Total amount: {total:,.2f}
        Interest amount: {interest_amount:,.2f}
        Total payment: {total_payment:,.2f}
        """
        messagebox.showinfo("EMI Calculation Result", result_text)

        # Call the function to plot the graph
        plot_graph(total, interest_rate, total_months, emi)  # Plotting the EMI breakdown graph

    except ValueError:
        # Show an error message if the input values are invalid.
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

def plot_graph(total, interest_rate, total_months, emi):
    # Prepare data for plotting
    balances = []
    interests = []
    capitals = []
    
    balance = total
    monthly_interest_rate = interest_rate / (12 * 100)

    # Calculate balance, interest, and capital for each month
    for month in range(1, total_months + 1):
        interest_payment = balance * monthly_interest_rate
        principal_payment = emi - interest_payment
        balance -= principal_payment

        balances.append(balance)
        interests.append(interest_payment)
        capitals.append(principal_payment)

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, total_months + 1), balances, label='Balance', color='blue')
    plt.plot(range(1, total_months + 1), interests, label='Interest', color='red')
    plt.plot(range(1, total_months + 1), capitals, label='Capital', color='green')

    plt.title('EMI Payment Breakdown Over Time')  
    plt.xlabel('Months')  
    plt.ylabel('Amount')  
    plt.legend() 
    plt.grid()  
    plt.tight_layout()  
    plt.show()  

# Clears all input fields to reset the form.
def clear_fields():
    # Clear the total amount entry.
    total_entry.delete(0, tk.END)  
    # Reset years to 0.
    years_var.set("0")              
    # Reset months to 1.
    months_var.set("1")             
    # Clear the interest rate entry.
    interest_entry.delete(0, tk.END) 

# Validates if the input can be converted to a float.
def validate_float(action, value_if_allowed):
    # If the action is '1', it means we are trying to insert something.
    if action == '1':  
        try:
            float(value_if_allowed)  
            return True  
        except ValueError:
            return False  
    return True  

# Validates if the input is a valid integer (digits only).
def validate_int(action, value_if_allowed):
    if action == '1':  
        return value_if_allowed.isdigit()
    return True  

# Create the main window
root = tk.Tk()
root.title("EMI Calculator by David Caleb")
root.configure(bg="#2E2E2E")

# Register validation commands
vcmd_float = (root.register(validate_float), '%d', '%P')  # Register float validation command
vcmd_int = (root.register(validate_int), '%d', '%P')  # Register integer validation command

# Create and place labels and entry fields with improved styling
label_style = {'bg': "#2E2E2E", 'fg': "#FFFFFF", 'font': ('Arial', 12)}  # Define label style
entry_style = {'bg': "#4B4B4B", 'fg': "#FFFFFF", 'font': ('Arial', 12)}  # Define entry field style

tk.Label(root, text="Total:", **label_style).grid(row=0, column=0, padx=10, pady=10, sticky='e')  # Total label
total_entry = tk.Entry(root, **entry_style, validate='key', validatecommand=vcmd_float)  # Total entry field with validation
total_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Years:", **label_style).grid(row=1, column=0, padx=10, pady=10, sticky='e')  # Years label
years_var = tk.StringVar(value="0")  # Initialize years variable
years_spinbox = ttk.Spinbox(root, from_=0, to=30, textvariable=years_var, width=5, validate='key', validatecommand=vcmd_int)  # Years spinbox with validation
years_spinbox.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Months:", **label_style).grid(row=2, column=0, padx=10, pady=10, sticky='e')  # Months label
months_var = tk.StringVar(value="1")  # Initialize months variable
months_spinbox = ttk.Spinbox(root, from_=1, to=11, textvariable=months_var, width=5, validate='key', validatecommand=vcmd_int)  # Months spinbox with validation
months_spinbox.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Interest rate (%):", **label_style).grid(row=3, column=0, padx=10, pady=10, sticky='e')  # Interest rate label
interest_entry = tk.Entry(root, **entry_style, validate='key', validatecommand=vcmd_float)  # Interest entry field with validation
interest_entry.grid(row=3, column=1, padx=10, pady=10)

# Create and place the calculate and clear buttons
button_style = {'bg': "#5A5A5A", 'fg': "#FFFFFF", 'font': ('Arial', 12)}  # Define button style

calculate_button = tk.Button(root, text="Calculate", command=calculate_emi, **button_style)  # Calculate button
calculate_button.grid(row=4, column=0, padx=10, pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_fields, **button_style)  # Clear button
clear_button.grid(row=4, column=1, padx=10, pady=10)

# Run the main event loop
root.mainloop()