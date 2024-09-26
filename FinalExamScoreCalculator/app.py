# Import necessary libraries
import tkinter as tk
from tkinter import ttk, messagebox

class FinalExamCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Final Exam Score Calculator by David Caleb")
        
        # Set the background color
        self.root.configure(bg="#2E2E2E")

        # Lists to store score and percentage entries
        self.scores = []
        self.percentages = []
        self.entry_widgets = []  # List to store entry widgets
        
        # Counter for dynamic input fields
        self.entry_count = 0
        
        # Initial instruction label
        tk.Label(root, text="Add your scores and percentages (0.0 - 5.0 for scores and 0-100 for percentages)",
                bg="#2E2E2E", fg="#FFFFFF", wraplength=400, justify="center").grid(row=0, column=0, columnspan=4, pady=10)

        # Button to add new input fields
        self.btn_add_input = tk.Button(root, text="Add New Input", command=self.add_input, bg="#4CAF50", fg="#FFFFFF")
        self.btn_add_input.grid(row=1, column=0, columnspan=4, pady=10)

        # Button to calculate the final score needed
        self.btn_calculate = tk.Button(root, text="Calculate Final Score Needed", command=self.calculate_final_score, bg="#2196F3", fg="#FFFFFF")
        self.btn_calculate.grid(row=2, column=0, columnspan=4, pady=10)

        # Label to show the result
        self.lbl_result = tk.Label(root, text="", bg="#2E2E2E", fg="#FFFFFF", wraplength=400, justify="center")
        self.lbl_result.grid(row=3, column=0, columnspan=4, padx=10, pady=10)
        
        # Button to reset entries
        self.btn_reset = tk.Button(root, text="Reset", command=self.reset_entries, bg="#F44336", fg="#FFFFFF")
        self.btn_reset.grid(row=4, column=0, columnspan=4, pady=10)

        # Progress bar
        self.progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
        self.progress.grid(row=5, column=0, columnspan=4, pady=10)
        
        # Configure columns to be responsive
        for i in range(4):
            root.columnconfigure(i, weight=1)

    # Add new input fields for scores and percentages
    def add_input(self):
        row_position = self.entry_count + 6
        
        # Labels and entry fields for scores and percentages
        lbl_score = tk.Label(self.root, text=f"Score {self.entry_count + 1} (0.0 - 5.0):", bg="#2E2E2E", fg="#FFFFFF")
        lbl_score.grid(row=row_position, column=0, padx=5, pady=5, sticky="e")
        
        entry_score = tk.Entry(self.root)
        entry_score.grid(row=row_position, column=1, padx=5, pady=5, sticky="ew")
        
        lbl_percentage = tk.Label(self.root, text=f"Percentage {self.entry_count + 1} (0 - 100):", bg="#2E2E2E", fg="#FFFFFF")
        lbl_percentage.grid(row=row_position, column=2, padx=5, pady=5, sticky="e")
        
        entry_percentage = tk.Entry(self.root)
        entry_percentage.grid(row=row_position, column=3, padx=5, pady=5, sticky="ew")

        # Append entries to the lists
        self.scores.append(entry_score)
        self.percentages.append(entry_percentage)
        
        # Store the widgets in a list for later deletion
        self.entry_widgets.append((lbl_score, entry_score, lbl_percentage, entry_percentage))
        
        # Update the entry count
        self.entry_count += 1

    # Calculate the required final score
    def calculate_final_score(self):
        try:
            total_score = 0.0
            total_percentage = 0.0
            
            # Process each input entry for score and percentage
            for score_entry, percentage_entry in zip(self.scores, self.percentages):
                score = float(score_entry.get())
                percentage = float(percentage_entry.get())
                
                # Validate inputs
                if not (0.0 <= score <= 5.0):
                    messagebox.showerror("Invalid Input", "The score must be between 0.0 and 5.0")
                    return
                if not (0.0 <= percentage <= 100.0):
                    messagebox.showerror("Invalid Input", "The percentage must be between 0 and 100")
                    return
                
                # Calculate cumulative score and percentage
                total_score += score * (percentage / 100)
                total_percentage += percentage
            
            # Check if the total percentage exceeds 100
            if total_percentage > 100.0:
                messagebox.showerror("Invalid Input", "The total percentage cannot exceed 100")
                return
            
            remaining_percentage = 100.0 - total_percentage
            
            if remaining_percentage <= 0:
                messagebox.showerror("Invalid Input", "The total percentage has already reached or exceeded 100%")
                return
            
            # Calculate the required score for the final exam
            required_final_score = (3.0 - total_score) / (remaining_percentage / 100)
            self.progress['value'] = total_percentage  # Update progress bar
            
            # Provide motivational messages based on the result
            if required_final_score <= 5.0:
                result_text = f"You need at least {required_final_score:.2f} in your final exam to pass.\nKeep going! Remember, hard work pays off!"
                if required_final_score < 2.0:
                    result_text += "\nYou're doing great! Maintain this pace, and success is guaranteed."
                elif required_final_score > 4.0:
                    result_text += "\nYou have some work to do, but it's still possible! Focus and push through."
            else:
                result_text = "Unfortunately, you need more than 5.0 to pass.\nTry harder next semester. Learn from this experience!"

            # Display the result
            self.lbl_result.config(text=result_text)
        
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for the scores and percentages.")

    # Reset all input fields and the progress bar
    def reset_entries(self):
        for widgets in self.entry_widgets:
            for widget in widgets:
                widget.destroy()
        
        self.scores.clear()
        self.percentages.clear()
        self.entry_widgets.clear()
        self.entry_count = 0
        self.lbl_result.config(text="")
        self.progress['value'] = 0

# Initialize the main application window
if __name__ == "__main__":
    root = tk.Tk()
    app = FinalExamCalculator(root)
    root.mainloop()