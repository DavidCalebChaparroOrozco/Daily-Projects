# Import necessary libraries
import tkinter as tk
import random
from tkinter import messagebox

# Function to generate random lottery numbers
def generate_lottery_numbers():
    return sorted(random.sample(range(1, 50), 6))

# Function to check if the user's numbers match the lottery numbers
def check_numbers():
    try:
        # Get the user's numbers from the entry boxes
        user_numbers = [
            int(entry_1.get()), int(entry_2.get()), int(entry_3.get()),
            int(entry_4.get()), int(entry_5.get()), int(entry_6.get())
        ]
    except ValueError:
        # Show error message if invalid input is provided
        messagebox.showerror("Invalid input", "Please enter valid numbers between 1 and 49.")
        return

    # Validate that the numbers are in the correct range
    if any(num < 1 or num > 49 for num in user_numbers):
        messagebox.showerror("Invalid input", "Numbers must be between 1 and 49.")
        return

    if len(set(user_numbers)) != 6:
        messagebox.showerror("Invalid input", "Please enter 6 unique numbers.")
        return

    # Generate random lottery numbers
    lottery_numbers = generate_lottery_numbers()

    # Find the matching numbers
    matching_numbers = set(user_numbers) & set(lottery_numbers)

    # Display the result to the user
    result_message = f"Your numbers: {sorted(user_numbers)}\nLottery numbers: {lottery_numbers}\n"
    result_message += f"Matching numbers: {sorted(matching_numbers)}\n"
    result_message += f"Total matches: {len(matching_numbers)}"

    if len(matching_numbers) == 6:
        result_message += "\nCongratulations! You won the lottery!"
    else:
        result_message += "\nBetter luck next time!"

    messagebox.showinfo("Lottery Results", result_message)

# Create the main window
root = tk.Tk()
root.title("Lottery Simulator by David Caleb")
root.geometry("400x200")

# Create a frame to center the content
frame = tk.Frame(root)
frame.pack(expand=True)

# Create labels and entry boxes for user input
label = tk.Label(frame, text="Enter 6 numbers between 1 and 49:")
label.pack(pady=10)

entry_frame = tk.Frame(frame)
entry_frame.pack(pady=5)

entry_1 = tk.Entry(entry_frame, width=5)
entry_1.grid(row=0, column=0)
entry_2 = tk.Entry(entry_frame, width=5)
entry_2.grid(row=0, column=1)
entry_3 = tk.Entry(entry_frame, width=5)
entry_3.grid(row=0, column=2)
entry_4 = tk.Entry(entry_frame, width=5)
entry_4.grid(row=0, column=3)
entry_5 = tk.Entry(entry_frame, width=5)
entry_5.grid(row=0, column=4)
entry_6 = tk.Entry(entry_frame, width=5)
entry_6.grid(row=0, column=5)

# Create a button to check the lottery numbers
check_button = tk.Button(frame, text="Check Lottery", command=check_numbers)
check_button.pack(pady=10)

# Run the main event loop
root.mainloop()