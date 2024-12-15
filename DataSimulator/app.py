# Importing necessary libraries
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to generate synthetic data based on selected distribution
def generate_data():
    try:
        # Get the number of samples from the entry field
        num_samples = int(num_samples_entry.get())
        
        # Get selected distribution type
        distribution = distribution_var.get()

        # Initialize an empty list for the generated data
        data = []

        # Generate data based on the selected distribution
        if distribution == "Normal":
            mean = float(mean_entry.get())
            std_dev = float(std_dev_entry.get())
            data = np.random.normal(mean, std_dev, num_samples)
        
        elif distribution == "Uniform":
            low = float(low_entry.get())
            high = float(high_entry.get())
            data = np.random.uniform(low, high, num_samples)
        
        elif distribution == "Binomial":
            n = int(n_entry.get())
            p = float(p_entry.get())
            data = np.random.binomial(n, p, num_samples)

        elif distribution == "Poisson":
            lam = float(lam_entry.get())
            data = np.random.poisson(lam, num_samples)

        else:
            messagebox.showerror("Error", "Please select a valid distribution.")
            return
        
        # Convert the generated data to a DataFrame for easier manipulation
        global generated_df
        generated_df = pd.DataFrame(data, columns=["Generated Data"])
        
        messagebox.showinfo("Success", "Data generated successfully!")
        
        # Call function to plot the histogram of the generated data
        plot_data()

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# Function to plot histogram of generated data
def plot_data():
    if 'generated_df' in globals():
        plt.style.use('dark_background')
        plt.figure(figsize=(10, 6))
        plt.hist(generated_df["Generated Data"], bins=30, alpha=0.7)
        plt.title("Histogram of Generated Data")
        plt.xlabel("Value", color="white")
        plt.ylabel("Frequency")
        plt.grid(color="gray")
        plt.show()

# Function to save the generated dataset as a CSV file
def save_data():
    if 'generated_df' not in globals():
        messagebox.showerror("Error", "No data generated yet.")
        return
    
    # Ask user for file path to save the CSV
    file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                            filetypes=[("CSV files", "*.csv"),
                                                        ("All files", "*.*")])
    if file_path:
        generated_df.to_csv(file_path, index=False)
        messagebox.showinfo("Success", "Data saved successfully!")

# Validate inputs and enable/disable buttons accordingly
def validate_inputs(*args):
    try:
        num_samples = int(num_samples_entry.get())
        
        if distribution_var.get() == "Normal":
            mean = float(mean_entry.get())
            std_dev = float(std_dev_entry.get())
            valid = num_samples > 0 and std_dev > 0
        
        elif distribution_var.get() == "Uniform":
            low = float(low_entry.get())
            high = float(high_entry.get())
            valid = num_samples > 0 and low < high
        
        elif distribution_var.get() == "Binomial":
            n = int(n_entry.get())
            p = float(p_entry.get())
            valid = num_samples > 0 and 0 <= p <= 1
        
        elif distribution_var.get() == "Poisson":
            lam = float(lam_entry.get())
            valid = num_samples > 0 and lam >= 0
            
        else:
            valid = False

    except ValueError:
        valid = False

    generate_button.config(state=tk.NORMAL if valid else tk.DISABLED)

# Create main application window
app = tk.Tk()
app.title("Synthetic Data Generator by David Caleb")
app.config(background="#2E2E2E")

# Distribution selection
distribution_var = tk.StringVar(value="Normal")
ttk.Label(app, text="Select Distribution:", background="#2E2E2E", foreground="white").grid(column=0, row=0)
distribution_menu = ttk.Combobox(app, textvariable=distribution_var,
                                values=["Normal", "Uniform", "Binomial", "Poisson"])
distribution_menu.grid(column=1, row=0)

# Number of samples input
ttk.Label(app, text="Number of Samples:", background="#2E2E2E", foreground="white").grid(column=0, row=1)
num_samples_entry = ttk.Entry(app)
num_samples_entry.grid(column=1, row=1)

# Normal distribution parameters
ttk.Label(app, text="Mean:", background="#2E2E2E", foreground="white").grid(column=0, row=2)
mean_entry = ttk.Entry(app)
mean_entry.grid(column=1, row=2)

ttk.Label(app, text="Standard Deviation:", background="#2E2E2E", foreground="white").grid(column=0, row=3)
std_dev_entry = ttk.Entry(app)
std_dev_entry.grid(column=1, row=3)

# Uniform distribution parameters
ttk.Label(app, text="Low (Uniform):", background="#2E2E2E", foreground="white").grid(column=0, row=4)
low_entry = ttk.Entry(app)
low_entry.grid(column=1, row=4)

ttk.Label(app, text="High (Uniform):", background="#2E2E2E", foreground="white").grid(column=0, row=5)
high_entry = ttk.Entry(app)
high_entry.grid(column=1, row=5)

# Binomial distribution parameters
ttk.Label(app, text="n (Binomial):", background="#2E2E2E", foreground="white").grid(column=0, row=6)
n_entry = ttk.Entry(app)
n_entry.grid(column=1, row=6)

ttk.Label(app, text="p (Binomial):", background="#2E2E2E", foreground="white").grid(column=0, row=7)
p_entry = ttk.Entry(app)
p_entry.grid(column=1, row=7)

# Poisson distribution parameters
ttk.Label(app, text="λ (Poisson):", background="#2E2E2E", foreground="white").grid(column=0, row=8)
lam_entry = ttk.Entry(app)
lam_entry.grid(column=1, row=8)

# Generate and Save buttons
generate_button = ttk.Button(app, text="Generate Data", command=generate_data)
generate_button.grid(column=0, row=9)

save_button = ttk.Button(app, text="Save Data as CSV", command=save_data)
save_button.grid(column=1, row=9)

# Bind input validation to entry fields and dropdown menu changes
num_samples_var = tk.StringVar()
num_samples_var.trace_add('write', validate_inputs)
num_samples_entry.config(textvariable=num_samples_var)

mean_var = tk.StringVar()
mean_var.trace_add('write', validate_inputs)
mean_entry.config(textvariable=mean_var)

std_dev_var = tk.StringVar()
std_dev_var.trace_add('write', validate_inputs)
std_dev_entry.config(textvariable=std_dev_var)

low_var = tk.StringVar()
low_var.trace_add('write', validate_inputs)
low_entry.config(textvariable=low_var)

high_var = tk.StringVar()
high_var.trace_add('write', validate_inputs)
high_entry.config(textvariable=high_var)

n_var = tk.StringVar()
n_var.trace_add('write', validate_inputs)
n_entry.config(textvariable=n_var)

p_var = tk.StringVar()
p_var.trace_add('write', validate_inputs)
p_entry.config(textvariable=p_var)

lam_var = tk.StringVar()
lam_var.trace_add('write', validate_inputs)
lam_entry.config(textvariable=lam_var)

# Validate when distribution changes
distribution_var.trace('w', validate_inputs)  

# Run the application
app.mainloop()
