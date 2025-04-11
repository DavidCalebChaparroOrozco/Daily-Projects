# Import necessary libraries
import tkinter as tk
from tkinter import messagebox
import random
import time
import math

class FortuneRoulette:
    # Initialize the Fortune Roulette application.
    def __init__(self, root):
        self.root = root
        self.root.title("Random Fortune Roulette by David Caleb")
        self.root.geometry("600x750")
        self.root.resizable(False, False)
        
        # Default options for the roulette
        self.default_options = ["Kaggle", "LeetCode", "OOP", "Recursion", "Machine Learning", "Data Science", "Basketball"]
        self.current_options = self.default_options.copy()
        
        # Animation variables
        self.is_spinning = False
        self.spin_angle = 0
        self.spin_speed = 0
        self.selected_option = None
        
        # Create UI elements
        self.create_widgets()
        
    # Create all the widgets for the application.
    def create_widgets(self):
        # Main title
        title_label = tk.Label(self.root, text="Random Fortune Roulette", font=("Arial", 20, "bold"))
        title_label.pack(pady=10)
        
        # Options frame
        options_frame = tk.LabelFrame(self.root, text="Roulette Options", padx=10, pady=10)
        options_frame.pack(pady=10, padx=20, fill="both")
        
        # Options entry
        self.options_text = tk.Text(options_frame, height=5, width=50)
        self.options_text.pack()
        self.options_text.insert("1.0", "\n".join(self.default_options))
        
        # Update options button
        update_btn = tk.Button(options_frame, text="Update Options", command=self.update_options)
        update_btn.pack(pady=5)
        
        # Roulette canvas
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.pack(pady=10)
        
        # Spin button
        spin_btn = tk.Button(self.root, text="SPIN!", command=self.start_spin, font=("Arial", 14, "bold"), bg="#4CAF50", fg="white")
        spin_btn.pack(pady=10)
        
        # Draw initial roulette
        self.draw_roulette()
        
    # Update the roulette options based on user input.
    def update_options(self):
        text = self.options_text.get("1.0", "end-1c")
        new_options = [opt.strip() for opt in text.split("\n") if opt.strip()]
        
        if len(new_options) < 2:
            messagebox.showerror("Error", "Please enter at least 2 options.")
            return
            
        self.current_options = new_options
        self.draw_roulette()
        
    # Draw the roulette wheel on the canvas.
    def draw_roulette(self):
        self.canvas.delete("all")
        center_x, center_y = 200, 200
        radius = 180
        
        # Draw the outer circle
        self.canvas.create_oval(center_x - radius, center_y - radius, 
                                center_x + radius, center_y + radius, 
                                outline="black", width=3)
        
        # Calculate angle for each option
        option_count = len(self.current_options)
        angle_per_option = 360 / option_count
        
        # Draw each segment
        for i, option in enumerate(self.current_options):
            start_angle = i * angle_per_option + self.spin_angle
            end_angle = (i + 1) * angle_per_option + self.spin_angle
            
            # Calculate coordinates for the arc
            x1 = center_x - radius * math.cos(math.radians(start_angle))
            y1 = center_y - radius * math.sin(math.radians(start_angle))
            x2 = center_x - radius * math.cos(math.radians(end_angle))
            y2 = center_y - radius * math.sin(math.radians(end_angle))
            
            # Create the arc
            self.canvas.create_arc(center_x - radius, center_y - radius,
                                    center_x + radius, center_y + radius,
                                    start=start_angle, extent=angle_per_option,
                                    fill=self.get_color(i), outline="black")
            
            # Calculate text position (middle of the segment)
            text_angle = (start_angle + angle_per_option / 2) % 360
            text_radius = radius * 0.6
            text_x = center_x + text_radius * math.cos(math.radians(text_angle))
            text_y = center_y - text_radius * math.sin(math.radians(text_angle))
            
            # Add the option text
            self.canvas.create_text(text_x, text_y, text=option, 
                                    angle=-text_angle, 
                                    font=("Arial", 10, "bold"))
        
        # Draw the center pointer
        pointer_length = 20
        self.canvas.create_line(center_x, center_y - radius, 
                                center_x, center_y - radius + pointer_length, 
                                width=3, fill="red")
        
    # Get a color for the roulette segment based on its index.
    def get_color(self, index):
        colors = ["#FF5733", "#33FF57", "#3357FF", "#F3FF33", "#FF33F3",
                    "#33FFF3", "#F333FF", "#FF8C33", "#8CFF33", "#338CFF"]
        return colors[index % len(colors)]
    
    # Start the spinning animation if not already spinning.
    def start_spin(self):
        if not self.is_spinning:
            self.is_spinning = True
            # Initial speed
            self.spin_speed = 30  
            self.selected_option = None
            self.spin()
    
    # Perform the spinning animation with gradual slowdown.
    def spin(self):
        if self.spin_speed > 0:
            # Continue spinning
            self.spin_angle = (self.spin_angle + self.spin_speed) % 360
            self.draw_roulette()
            
            # Gradually decrease speed
            self.spin_speed = max(0, self.spin_speed - 0.5)
            
            # Schedule next frame
            self.root.after(30, self.spin)
        else:
            # Spinning has stopped
            self.is_spinning = False
            self.show_result()
    
    # Determine and display the selected option.
    def show_result(self):
        # Calculate which option is selected based on the final angle
        option_count = len(self.current_options)
        angle_per_option = 360 / option_count
        
        # The pointer is at 90 degrees (top), so we adjust for that
        adjusted_angle = (360 - self.spin_angle + 90) % 360
        selected_index = int(adjusted_angle // angle_per_option)
        
        # Ensure index is within bounds
        selected_index = min(selected_index, option_count - 1)
        self.selected_option = self.current_options[selected_index]
        
        # Show result in a message box
        messagebox.showinfo("Result", f"The selected option is:\n\n{self.selected_option}")

# Main function to run the application.
def main():
    root = tk.Tk()
    app = FortuneRoulette(root)
    root.mainloop()

if __name__ == "__main__":
    main()