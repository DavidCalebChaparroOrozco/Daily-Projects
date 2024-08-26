# Importing necessary libraries
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# List to store the calculation history
history = []

# Calculates the Body Mass Index (BMI) from weight and height in cm.
def calculate_bmi(weight, height_cm):
    # Convert centimeters to meters
    height_m = height_cm / 100  
    return weight / (height_m ** 2)

# Provides health recommendations based on the BMI.
def determine_health_recommendation(bmi):
    if bmi < 18.5:
        return "It is advisable to consult a nutritionist for a dietary plan to help you reach a healthy weight."
    elif 18.5 <= bmi < 24.9:
        return "Maintain a balanced diet and regular exercise to keep your healthy weight."
    elif 25 <= bmi < 29.9:
        return "Consider implementing healthy eating habits and physical activity to reduce your weight."
    else:
        return "It is important to seek medical guidance for an appropriate and safe weight loss plan."

# Calculates the BMI and displays the result in the interface.
def calculate():
    try:
        weight = float(entry_weight.get())
        height_cm = float(entry_height.get())
        
        bmi = calculate_bmi(weight, height_cm)
        recommendation = determine_health_recommendation(bmi)
        
        bmi_result.set(f"Your BMI is: {bmi:.2f}")
        recommendation_result.set(f"Recommendation: {recommendation}")
        
        # Change background color based on BMI
        if bmi < 18.5:
            window.config(bg="lightblue")
        elif 18.5 <= bmi < 24.9:
            window.config(bg="lightgreen")
        elif 25 <= bmi < 29.9:
            window.config(bg="orange")
        else:
            window.config(bg="red")
        
        # Save to history
        history.append((weight, height_cm, bmi))
        update_history()
        show_bmi_graph()
        show_weight_graph()
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for weight and height.")

# Updates the history list in the interface.
def update_history():
    history_listbox.delete(0, tk.END)
    for idx, (weight, height, bmi) in enumerate(history[-5:], 1):
        history_listbox.insert(tk.END, f"{idx}. Weight: {weight} kg, Height: {height} cm, BMI: {bmi:.2f}")

# Resets the input fields and results.
def reset():
    entry_weight.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    bmi_result.set("")
    recommendation_result.set("")
    window.config(bg="SystemButtonFace") 

# Saves the history to a JSON file.
def save_history():
    with open("bmi_history.json", "w") as file:
        json.dump(history, file)
    messagebox.showinfo("Saved", "History saved successfully.")

# Loads the history from a JSON file.
def load_history():
    global history
    try:
        with open("bmi_history.json", "r") as file:
            history = json.load(file)
        update_history()
        messagebox.showinfo("Loaded", "History loaded successfully.")
    except FileNotFoundError:
        messagebox.showerror("Error", "History file not found.")
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Error reading history file.")

# Displays a graph of BMI evolution.
def show_bmi_graph():
    if len(history) < 2:
        # Do not show the graph if there are fewer than 2 entries in the history
        return  

    bmis = [h[2] for h in history]
    indices = list(range(1, len(history) + 1))
    
    fig, ax = plt.subplots()
    ax.plot(indices, bmis, marker='o')
    ax.set_xlabel("Measurement")
    ax.set_ylabel("BMI")
    ax.set_title("BMI Evolution")
    
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(row=11, column=0, columnspan=2)
    canvas.draw()

# Displays a graph of weight evolution.
def show_weight_graph():
    if len(history) < 2:
        # Do not show the graph if there are fewer than 2 entries in the history
        return  

    weights = [h[0] for h in history]
    indices = list(range(1, len(history) + 1))
    
    fig, ax = plt.subplots()
    ax.plot(indices, weights, marker='o', color='blue')
    ax.set_xlabel("Measurement")
    ax.set_ylabel("Weight (kg)")
    ax.set_title("Weight Evolution")
    
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(row=12, column=0, columnspan=2)
    canvas.draw()

# Create the main window
window = tk.Tk()
window.title("BMI Calculator by David Caleb")

# Set a fixed size for the window

window.resizable(False, False)

# Create and place components in the window
tk.Label(window, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=10)
entry_weight = ttk.Entry(window)
entry_weight.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Height (cm):").grid(row=1, column=0, padx=10, pady=10)
entry_height = ttk.Entry(window)
entry_height.grid(row=1, column=1, padx=10, pady=10)

ttk.Button(window, text="Calculate BMI", command=calculate).grid(row=2, column=0, columnspan=2, pady=10)

bmi_result = tk.StringVar()
ttk.Label(window, textvariable=bmi_result).grid(row=3, column=0, columnspan=2, pady=10)

# History
ttk.Label(window, text="Calculation History:").grid(row=6, column=0, columnspan=2, pady=10)
history_listbox = tk.Listbox(window, width=50)
history_listbox.grid(row=7, column=0, columnspan=2, pady=10)

# Button to reset
ttk.Button(window, text="Reset", command=reset).grid(row=8, column=0, columnspan=2, pady=10)

# Buttons to save and load history
ttk.Button(window, text="Save History", command=save_history).grid(row=9, column=0, pady=10)
ttk.Button(window, text="Load History", command=load_history).grid(row=9, column=1, pady=10)

# Label for recommendations
recommendation_result = tk.StringVar()
ttk.Label(window, textvariable=recommendation_result, wraplength=300).grid(row=10, column=0, columnspan=2, pady=10)

# Start the main loop of the interface
window.mainloop()