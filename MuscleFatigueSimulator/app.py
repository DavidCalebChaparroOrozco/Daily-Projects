# Importing necessary libraries
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
import csv
from fpdf import FPDF
import datetime

# Predefined muscle groups
MUSCLE_GROUPS = ["Arms", "Legs", "Back", "Chest", "Shoulders", "Core"]

# Handles database operations for saving and retrieving workout history.
class Database:
    def __init__(self):
        # Connect to SQLite database (or create it if it doesn't exist)
        self.conn = sqlite3.connect("workout_history.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    # Create the workouts table if it doesn't exist.
    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY,
            date TEXT,
            muscle_group TEXT,
            initial_energy REAL,
            fatigue_rate REAL,
            energy_data TEXT
        )"""
        )
        self.conn.commit()

    # Save a workout to the database.
    def save_workout(self, date, muscle_group, initial_energy, fatigue_rate, energy_data):
        self.cursor.execute("""
        INSERT INTO workouts (date, muscle_group, initial_energy, fatigue_rate, energy_data)
        VALUES (?, ?, ?, ?, ?)""", (date, muscle_group, initial_energy, fatigue_rate, str(energy_data)))
        self.conn.commit()

    # Fetch all workouts from the database.
    def fetch_workouts(self):
        self.cursor.execute("SELECT * FROM workouts")
        return self.cursor.fetchall()

    # Close the database connection.
    def close(self):
        self.conn.close()

# Simulates muscle fatigue over multiple sets with personalized adjustments.
class MuscleFatigueSimulator:
    def __init__(self, initial_energy=100, fatigue_rate=0.15, min_energy_threshold=5, muscle_group="Arms", age=25, weight=70, fitness_level="Intermediate"):
        self.initial_energy = initial_energy
        self.fatigue_rate = self.adjust_fatigue_rate(fatigue_rate, age, weight, fitness_level)
        self.min_energy_threshold = min_energy_threshold
        # Stores energy levels after each set
        self.energy_data = []  
        self.muscle_group = muscle_group

    # Adjust fatigue rate based on personal data.
    def adjust_fatigue_rate(self, base_rate, age, weight, fitness_level):
        if fitness_level == "Beginner":
            # Higher fatigue for beginners
            return base_rate * 1.2  
        elif fitness_level == "Advanced":
            # Lower fatigue for advanced users
            return base_rate * 0.8  
        return base_rate

    # Simulate a single set and recursively perform the next set.
    def perform_set(self, current_energy, set_number, max_sets=20):
        if current_energy <= self.min_energy_threshold or set_number > max_sets:
            return 0  # Stop if energy is too low or max sets reached

        # Calculate energy loss and remaining energy
        energy_loss = current_energy * self.fatigue_rate
        remaining_energy = current_energy - energy_loss
        self.energy_data.append(remaining_energy)

        # Recursively perform the next set
        return self.perform_set(remaining_energy, set_number + 1, max_sets)

    # Start the exercise routine simulation.
    def start_routine(self):
        self.energy_data = [self.initial_energy]  
        self.perform_set(self.initial_energy, 1)

    # Return the energy data for plotting.
    def get_energy_data(self):
        return self.energy_data

    # Generate notifications based on energy levels.
    def get_notifications(self):
        notifications = []
        if self.energy_data[-1] < 20:
            notifications.append(f"{self.muscle_group} energy is low ({self.energy_data[-1]:.2f}%). Consider reducing weight or increasing rest time.")
        if len(self.energy_data) % 5 == 0:
            notifications.append(f"Completed {len(self.energy_data)} sets for {self.muscle_group}. Great job!")
        return notifications

# Main application GUI.
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Muscle Fatigue Simulator by David Caleb")
        self.root.configure(bg="#2C2F33")  
        self.simulator = None
        self.db = Database()  

        # Configure styles
        self.style = ttk.Style()
        self.style.configure("TLabel", foreground="white", background="#2C2F33", font=("Arial", 12))
        self.style.configure("TButton", foreground="black", background="#7289DA", font=("Arial", 12))
        self.style.configure("TCombobox", font=("Arial", 12))

        # Input fields
        ttk.Label(root, text="Initial Energy (%)").grid(row=0, column=0, padx=10, pady=10)
        self.initial_energy_entry = ttk.Entry(root)
        self.initial_energy_entry.grid(row=0, column=1, padx=10, pady=10)
        self.initial_energy_entry.insert(0, "100")

        ttk.Label(root, text="Fatigue Rate (%)").grid(row=1, column=0, padx=10, pady=10)
        self.fatigue_rate_entry = ttk.Entry(root)
        self.fatigue_rate_entry.grid(row=1, column=1, padx=10, pady=10)
        self.fatigue_rate_entry.insert(0, "15")

        ttk.Label(root, text="Muscle Group").grid(row=2, column=0, padx=10, pady=10)
        self.muscle_group_var = tk.StringVar()
        self.muscle_group_combo = ttk.Combobox(root, textvariable=self.muscle_group_var, values=MUSCLE_GROUPS, state="readonly")
        self.muscle_group_combo.grid(row=2, column=1, padx=10, pady=10)
        self.muscle_group_combo.set(MUSCLE_GROUPS[0])

        ttk.Label(root, text="Age").grid(row=3, column=0, padx=10, pady=10)
        self.age_entry = ttk.Entry(root)
        self.age_entry.grid(row=3, column=1, padx=10, pady=10)

        ttk.Label(root, text="Weight (kg)").grid(row=4, column=0, padx=10, pady=10)
        self.weight_entry = ttk.Entry(root)
        self.weight_entry.grid(row=4, column=1, padx=10, pady=10)

        ttk.Label(root, text="Fitness Level").grid(row=5, column=0, padx=10, pady=10)
        self.fitness_level_var = tk.StringVar()
        self.fitness_level_combo = ttk.Combobox(root, textvariable=self.fitness_level_var, values=["Beginner", "Intermediate", "Advanced"], state="readonly")
        self.fitness_level_combo.grid(row=5, column=1, padx=10, pady=10)
        self.fitness_level_combo.set("Intermediate")

        # Buttons
        ttk.Button(root, text="Start Routine", command=self.start_routine).grid(row=6, column=0, columnspan=2, pady=10)
        ttk.Button(root, text="Export to CSV", command=self.export_to_csv).grid(row=8, column=0, pady=10)
        ttk.Button(root, text="Export to PDF", command=self.export_to_pdf).grid(row=8, column=1, pady=10)
        ttk.Button(root, text="Show History", command=self.show_history).grid(row=9, column=0, columnspan=2, pady=10)

        # Plot area
        self.figure, self.ax = plt.subplots(figsize=(5, 5))
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().grid(row=7, column=0, columnspan=2, pady=10)

    # Start the simulation and plot the results.
    def start_routine(self):
        initial_energy = float(self.initial_energy_entry.get())
        fatigue_rate = float(self.fatigue_rate_entry.get()) / 100
        muscle_group = self.muscle_group_var.get()
        age = int(self.age_entry.get())
        weight = float(self.weight_entry.get())
        fitness_level = self.fitness_level_var.get()

        # Initialize simulator
        self.simulator = MuscleFatigueSimulator(initial_energy, fatigue_rate, muscle_group=muscle_group, age=age, weight=weight, fitness_level=fitness_level)
        self.simulator.start_routine()
        self.plot_energy()

        # Save workout to database
        self.db.save_workout(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), muscle_group, initial_energy, fatigue_rate, self.simulator.get_energy_data())

        # Show notifications
        notifications = self.simulator.get_notifications()
        if notifications:
            messagebox.showinfo("Notifications", "\n".join(notifications))

    # Plot the energy levels over sets.
    def plot_energy(self):
        self.ax.clear()
        self.ax.plot(self.simulator.get_energy_data(), marker='o', linestyle='-', color='b')
        self.ax.set_title(f"Energy Over Sets ({self.simulator.muscle_group})")
        self.ax.set_xlabel("Set Number")
        self.ax.set_ylabel("Energy (%)")
        self.ax.grid(True)
        self.canvas.draw()

    # Export energy data to a CSV file.
    def export_to_csv(self):
        if not self.simulator:
            messagebox.showwarning("No Data", "No workout data to export.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Set", "Energy (%)"])
                for i, energy in enumerate(self.simulator.get_energy_data()):
                    writer.writerow([i + 1, energy])
            messagebox.showinfo("Success", "Data exported to CSV successfully.")

    # Export energy data to a PDF file.
    def export_to_pdf(self):
        if not self.simulator:
            messagebox.showwarning("No Data", "No workout data to export.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=f"Workout Report - {self.simulator.muscle_group}", ln=True, align="C")
            pdf.cell(200, 10, txt="Set\tEnergy (%)", ln=True)
            for i, energy in enumerate(self.simulator.get_energy_data()):
                pdf.cell(200, 10, txt=f"{i + 1}\t{energy:.2f}", ln=True)
            pdf.output(file_path)
            messagebox.showinfo("Success", "Data exported to PDF successfully.")

    # Display workout history from the database.
    def show_history(self):
        workouts = self.db.fetch_workouts()
        if not workouts:
            messagebox.showinfo("History", "No workout history found.")
            return

        history_text = "\n".join([f"{row[1]} - {row[2]} (Energy: {row[3]}%, Fatigue: {row[4]})" for row in workouts])
        messagebox.showinfo("Workout History", history_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()