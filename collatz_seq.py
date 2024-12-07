# Importing necessary libraries
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog

# Generate the Collatz sequence for a given number.
def collatz_seq(n):
    seq = [n]
    while n != 1:
        # Even number
        if n % 2 == 0:
            n //= 2
        # Odd number
        else:
            n = 3 * n + 1
        seq.append(n)
    return seq

# Plot the Collatz sequence for a given number
def plot_collatz_seq(n):
    seq = collatz_seq(n)
    
    # Use dark background style
    plt.style.use('dark_background')
    
    plt.figure(figsize=(10, 6))
    plt.plot(seq, marker='o', linestyle='-', color='cyan', markersize=8)  
    plt.title(f"Collatz Conjecture Sequence for {n}", color='white')
    plt.xlabel("Step", color='white')
    plt.ylabel("Value", color='white')
    
    # Customize grid lines
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    
    # Change tick colors
    plt.tick_params(axis='both', colors='white')
    
    plt.show()

# Function to get user input through a GUI dialog
def get_user_input():
    root = tk.Tk()
    # Hide the main window
    root.withdraw()  
    try:
        number = simpledialog.askinteger("Input", "Enter a positive integer:", minvalue=1)
        if number is not None:
            plot_collatz_seq(number)
        else:
            print("No input provided.")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    get_user_input()