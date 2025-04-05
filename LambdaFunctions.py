# Import necessary libraries
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# Create the main application window
root = tk.Tk()
root.title("Lambda Function Plotter by David Caleb")
root.geometry("700x600")
root.configure(bg="#1e1e1e")

# Define fonts and colors
FONT = ("Segoe UI", 12)
ENTRY_BG = "#2d2d2d"
ENTRY_FG = "#ffffff"
BTN_BG = "#3c3f41"
BTN_FG = "#ffffff"
TEXT_COLOR = "#ffffff"

# Create a frame for input
input_frame = tk.Frame(root, bg="#1e1e1e")
input_frame.pack(pady=20)

# Label
label = tk.Label(input_frame, text="Enter a lambda function (e.g. lambda x: x**2 - 4*x + 3):", 
                    font=FONT, fg=TEXT_COLOR, bg="#1e1e1e")
label.pack(pady=5)

# Entry widget for user input
entry = tk.Entry(input_frame, font=FONT, width=50, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=ENTRY_FG)
entry.pack(pady=5)

# Create a frame for the plot
plot_frame = tk.Frame(root, bg="#1e1e1e")
plot_frame.pack(fill=tk.BOTH, expand=True)

# Get the user input, evaluate the lambda, and plot the function.
def plot_function():
    func_str = entry.get()
    try:
        user_func = eval(func_str)
        if not callable(user_func):
            raise ValueError("Input is not a valid lambda function.")
    except Exception as e:
        messagebox.showerror("Invalid Input", f"Error: {e}")
        return

    # Generate x and y values
    x = np.linspace(-10, 10, 1000)
    try:
        y = [user_func(val) for val in x]
    except Exception as e:
        messagebox.showerror("Evaluation Error", f"Error evaluating function: {e}")
        return

    # Clear previous plots
    for widget in plot_frame.winfo_children():
        widget.destroy()

    # Plot the function
    fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
    fig.patch.set_facecolor("#1e1e1e")  # Figure background
    ax.set_facecolor("#2b2b2b")         # Plot area background
    ax.plot(x, y, color="cyan", label="User Function")
    ax.axhline(0, color='white', linewidth=0.5)
    ax.axvline(0, color='white', linewidth=0.5)
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.set_title("Function Graph", color="white")
    ax.set_xlabel("x", color="white")
    ax.set_ylabel("f(x)", color="white")
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.legend(facecolor="#2b2b2b", edgecolor="white", labelcolor="white")

    # Embed the plot in the Tkinter GUI
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Button to plot
plot_button = tk.Button(root, text="Plot Function", font=FONT, command=plot_function,
                        bg=BTN_BG, fg=BTN_FG, activebackground="#505050", activeforeground="white",
                        relief=tk.FLAT, padx=10, pady=5)
plot_button.pack(pady=10)

# Run the GUI
root.mainloop()