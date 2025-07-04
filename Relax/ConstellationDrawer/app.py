# Import necessary libraries
import tkinter as tk
from tkinter import Canvas, Button, colorchooser

class ConstellationDrawer:
    def __init__(self, root):
        # Set initial window size
        self.root = root
        self.root.title("Constellation Drawer by David Caleb")
        self.root.geometry("1000x600") 

        # List to store star coordinates (x, y)
        self.stars = []  
        # List to store line coordinates and IDs
        self.lines = []  
        # Stores the (x, y) of the last clicked star for drawing lines
        self.current_line_start = None  
        # Default line color
        self.line_color = "white" 

        self.setup_ui()

    def setup_ui(self):
        # Create a canvas for drawing stars and lines
        self.canvas = Canvas(self.root, bg="black", width=800, height=500)
        self.canvas.pack(pady=10)

        # Bind mouse click event to the canvas
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        # Frame for buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)

        # Clear Button
        clear_button = Button(button_frame, text="Clear All", command=self.clear_all)
        clear_button.pack(side=tk.LEFT, padx=5)

        # Undo Last Line Button
        undo_button = Button(button_frame, text="Undo Last Line", command=self.undo_last_line)
        undo_button.pack(side=tk.LEFT, padx=5)

        # Change Line Color Button
        color_button = Button(button_frame, text="Change Line Color", command=self.choose_line_color)
        color_button.pack(side=tk.LEFT, padx=5)

        # Instructions Label
        instructions_label = tk.Label(self.root, text="Click to place stars. Click on two stars to connect them. Use buttons to manage your drawing.", fg="gray")
        instructions_label.pack(pady=5)

    def on_canvas_click(self, event):
        x, y = event.x, event.y
        star_radius = 5

        # Check if a star already exists at the clicked location (within a small radius)
        # This helps in connecting existing stars rather than creating new ones right next to them
        clicked_existing_star = False
        for i, (sx, sy) in enumerate(self.stars):
            if abs(sx - x) < star_radius * 2 and abs(sy - y) < star_radius * 2:
                # If an existing star is clicked
                clicked_existing_star = True
                if self.current_line_start:
                    # If we have a start point for a line, draw the line to this star
                    self.draw_line(self.current_line_start, (sx, sy))
                    self.current_line_start = None # Reset current line start after drawing
                else:
                    # If no current line start, this star becomes the start of a new line
                    self.current_line_start = (sx, sy)
                break

        # If no existing star was clicked, create a new one
        if not clicked_existing_star:
            # If there was a pending line start, drawing a new star should not connect to it
            self.draw_star(x, y, star_radius)
            # This new star becomes the potential start of a line
            self.current_line_start = (x, y) 

    # Draw a white circle to represent a star
    def draw_star(self, x, y, radius):
        star_id = self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="white", outline="white")
        # Store star coordinates
        self.stars.append((x, y)) 

    # Draw a line between two star coordinates
    def draw_line(self, start_coords, end_coords):
        x1, y1 = start_coords
        x2, y2 = end_coords
        line_id = self.canvas.create_line(x1, y1, x2, y2, fill=self.line_color, width=2)
        # Store the line ID to allow for undo
        self.lines.append(line_id) 

    # Delete all objects from the canvas
    def clear_all(self):
        self.canvas.delete("all")
        self.stars = []
        self.lines = []
        self.current_line_start = None

    def undo_last_line(self):
        if self.lines:
            # Get and remove the ID of the last drawn line
            last_line_id = self.lines.pop() 
            # Delete the line from the canvas
            self.canvas.delete(last_line_id) 

    # Open a color chooser dialog
    def choose_line_color(self):
        # [1] gives the hex code
        color_code = colorchooser.askcolor(title="Choose Line Color")[1] 
        # If a color was selected
        if color_code: 
            self.line_color = color_code

if __name__ == "__main__":
    root = tk.Tk()
    app = ConstellationDrawer(root)
    root.mainloop()