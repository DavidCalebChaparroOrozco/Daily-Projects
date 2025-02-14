# Importing necessary libraries
import tkinter as tk
from tkinter import messagebox
import unittest

# Josephus Problem Solver
def josephus(n, k):
    """
    Parameters:
    n: The number of people in the circle.
    k: The step size (number of people to skip before the next person is executed).

    Returns:
    int: The position of the last remaining person.
    """
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1


# Solves the Josephus problem and displays the elimination steps.
def josephus_with_steps(n, k):
    """
    Parameters:
    n: The number of people in the circle.
    k: The step size.

    Returns:
    int: The position of the last remaining person.
    list: List of steps showing the elimination process.
    """
    # Create a list representing the circle
    circle = list(range(1, n + 1))  
    index = 0
    steps = []

    steps.append(f"Initial circle: {circle}")
    while len(circle) > 1:
        # Calculate the index of the person to eliminate
        index = (index + k - 1) % len(circle)  
        # Remove the person from the circle
        eliminated = circle.pop(index)  
        steps.append(f"Eliminated person {eliminated}. Remaining circle: {circle}")
    
    steps.append(f"The last remaining person is at position: {circle[0]}")
    return circle[0], steps


# Initializes the Tkinter GUI for the Josephus Problem Solver.
class JosephusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Josephus Problem Solver by David Caleb")
        self.root.configure(bg="#2E3440")  # Dark background color

        # Custom font and colors
        self.label_font = ("Arial", 12)
        self.entry_font = ("Arial", 12)
        self.button_font = ("Arial", 12, "bold")
        self.text_font = ("Arial", 10)
        self.bg_color = "#2E3440"  
        self.fg_color = "#ECEFF4"   
        self.button_bg = "#4C566A"  
        self.button_fg = "#ECEFF4"  
        self.button_active_bg = "#5E81AC"  

        # Labels
        tk.Label(root, text="Number of people (n):", font=self.label_font, bg=self.bg_color, fg=self.fg_color).grid(row=0, column=0, padx=10, pady=10)
        tk.Label(root, text="Step size (k):", font=self.label_font, bg=self.bg_color, fg=self.fg_color).grid(row=1, column=0, padx=10, pady=10)

        # Entry fields
        self.n_entry = tk.Entry(root, font=self.entry_font, bg="#3B4252", fg=self.fg_color, insertbackground=self.fg_color)
        self.k_entry = tk.Entry(root, font=self.entry_font, bg="#3B4252", fg=self.fg_color, insertbackground=self.fg_color)
        self.n_entry.grid(row=0, column=1, padx=10, pady=10)
        self.k_entry.grid(row=1, column=1, padx=10, pady=10)

        # Buttons
        self.solve_button = tk.Button(root, text="Solve", font=self.button_font, bg=self.button_bg, fg=self.button_fg, activebackground=self.button_active_bg, activeforeground=self.fg_color, command=self.solve)
        self.solve_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Text box to display steps
        self.steps_text = tk.Text(root, height=10, width=50, font=self.text_font, bg="#3B4252", fg=self.fg_color, insertbackground=self.fg_color)
        self.steps_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # Solves the Josephus problem based on user input and displays the steps.
    def solve(self):
        try:
            # Get and validate inputs
            n = int(self.n_entry.get())
            k = int(self.k_entry.get())

            if n <= 0 or k <= 0:
                messagebox.showerror("Error", "Please enter positive integers for n and k.")
                return

            # Solve the problem and get steps
            survivor, steps = josephus_with_steps(n, k)

            # Display steps in the text box
            self.steps_text.delete(1.0, tk.END)
            for step in steps:
                self.steps_text.insert(tk.END, step + "\n")

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid integers.")


# Unit Tests
class TestJosephus(unittest.TestCase):
    def test_josephus(self):
        self.assertEqual(josephus(7, 3), 4)
        self.assertEqual(josephus(5, 2), 3)
        self.assertEqual(josephus(10, 4), 5)

    def test_josephus_with_steps(self):
        survivor, steps = josephus_with_steps(7, 3)
        self.assertEqual(survivor, 4)
        self.assertIn("Eliminated person 3", steps[1])


# Main Program
if __name__ == "__main__":
    # Run unit tests
    unittest.main(exit=False)

    # Start the Tkinter GUI
    root = tk.Tk()
    app = JosephusApp(root)
    root.mainloop()