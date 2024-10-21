# Importing necessary libraries
import tkinter as tk
from tkinter import colorchooser

# Function to open the color chooser dialog
def pick_color():
    # Open the color chooser dialog and store the selected color in 'color_code'
    color_code = colorchooser.askcolor(title="Choose a color")
    
    # If a color is selected (not None)
    if color_code[1]:
        # Set the background color of the window to the selected color
        color_display.config(bg=color_code[1])
        # Display the hexadecimal value of the color
        hex_value.set(f"Hex: {color_code[1]}")
        # Display the RGB value of the color
        rgb_value.set(f"RGB: {color_code[0]}")

# Create the main window with a dark background
root = tk.Tk()
root.title("Color Picker by David Caleb")
root.configure(bg="#2E2E2E")

# StringVar to hold the hexadecimal value of the selected color
hex_value = tk.StringVar()
hex_value.set("Hex: #FFFFFF")

# StringVar to hold the RGB value of the selected color
rgb_value = tk.StringVar()
rgb_value.set("RGB: (255, 255, 255)")

# Create a label to display the selected color with updated font and background
color_display = tk.Label(root, text="Selected Color", bg="#FFFFFF", font=("Trebuchet MS", 16), width=20, height=5)
color_display.pack(pady=20)

# Create a button to open the color picker with updated font
btn_pick_color = tk.Button(root, text="Pick a Color", command=pick_color, font=("Trebuchet MS", 14))
btn_pick_color.pack(pady=10)

# Create a label to display the hex code of the selected color with updated font
hex_label = tk.Label(root, textvariable=hex_value, font=("Trebuchet MS", 12), bg="#2E2E2E", fg="white")
hex_label.pack(pady=5)

# Create a label to display the RGB code of the selected color with updated font
rgb_label = tk.Label(root, textvariable=rgb_value, font=("Trebuchet MS", 12), bg="#2E2E2E", fg="white")
rgb_label.pack(pady=5)

# Start the Tkinter main loop
root.mainloop()