# Import necessary libraries
import turtle
import colorsys
import tkinter as tk
from tkinter import ttk
import datetime
from PIL import ImageGrab
import os

# Turtle Drawing Function with PNG saving
def draw_art(iterations=150, pensize=2.5, color_mode='rainbow', save_image=False):
    # Setup turtle screen
    screen = turtle.Screen()
    screen.title("Spiral Symphony")
    screen.bgcolor('black')
    screen.tracer(3)
    
    # Setup turtle
    artist = turtle.Turtle()
    artist.pensize(pensize)
    artist.speed(0)
    
    h = 0.7
    for i in range(iterations):
        if color_mode == 'rainbow':
            c = colorsys.hsv_to_rgb(h, 1, 1)
        elif color_mode == 'sunset':
            c = colorsys.hsv_to_rgb(h, 0.8, 0.9)
        elif color_mode == 'neon':
            c = colorsys.hsv_to_rgb(h, 1, 0.7)
        else:
            c = (1, 1, 1)

        artist.color(c)
        h += 0.004

        radius = max(190 - i, 20)
        artist.circle(radius, 90)
        artist.left(90)
        artist.left(22)
        artist.circle(radius, 90)
        artist.left(20)

    # Add signature
    artist.penup()
    artist.goto(0, 250)
    artist.pencolor("white")
    artist.write("Created by David Caleb - Spiral Symphony", align="center", font=("Arial", 12, "normal"))
    artist.hideturtle()
    
    # Update screen to ensure all drawing is complete
    screen.update()
    
    if save_image:
        # Get the turtle canvas
        canvas = screen.getcanvas()
        
        # Generate filename
        filename = f"SpiralSymphony.png"
        
        # Save as PNG using ImageGrab
        x0 = canvas.winfo_rootx()
        y0 = canvas.winfo_rooty()
        x1 = x0 + canvas.winfo_width()
        y1 = y0 + canvas.winfo_height()
        
        ImageGrab.grab(bbox=(x0, y0, x1, y1)).save(filename)
        print(f"Image saved as {filename}")
    
    turtle.done()

# GUI with Tkinter
def launch_gui():
    def start_drawing():
        try:
            iterations = int(iterations_var.get())
            pensize = float(pensize_var.get())
            color_mode = color_var.get()
            save_img = save_var.get()

            # Close GUI if requested
            if close_var.get():
                root.after(100, root.destroy)
            
            # Start drawing
            draw_art(iterations, pensize, color_mode, save_img)

        except Exception as e:
            print(f"Error: {e}")

    root = tk.Tk()
    root.title("Spiral Symphony - Controller")
    root.geometry("400x350")
    root.configure(bg="black")

    title = tk.Label(root, text="Spiral Symphony 🎨", bg="black", fg="white", font=("Arial", 16, "bold"))
    title.pack(pady=10)

    iterations_var = tk.StringVar(value="150")
    pensize_var = tk.StringVar(value="2.5")
    color_var = tk.StringVar(value="rainbow")
    save_var = tk.BooleanVar(value=True)
    close_var = tk.BooleanVar(value=False)

    frame = tk.Frame(root, bg="black")
    frame.pack(pady=10)

    tk.Label(frame, text="Iterations:", bg="black", fg="white").grid(row=0, column=0, sticky="w")
    tk.Entry(frame, textvariable=iterations_var, width=10).grid(row=0, column=1)

    tk.Label(frame, text="Pen Size:", bg="black", fg="white").grid(row=1, column=0, sticky="w")
    tk.Entry(frame, textvariable=pensize_var, width=10).grid(row=1, column=1)

    tk.Label(frame, text="Color Mode:", bg="black", fg="white").grid(row=2, column=0, sticky="w")
    ttk.Combobox(frame, textvariable=color_var, values=["rainbow", "sunset", "neon"], width=8).grid(row=2, column=1)

    tk.Checkbutton(frame, text="Save as PNG", variable=save_var, bg="black", fg="white", selectcolor="black").grid(row=3, column=0, columnspan=2, sticky="w")
    tk.Checkbutton(frame, text="Close GUI after start", variable=close_var, bg="black", fg="white", selectcolor="black").grid(row=4, column=0, columnspan=2, sticky="w")

    btn_frame = tk.Frame(root, bg="black")
    btn_frame.pack(pady=15)

    tk.Button(btn_frame, text="Start Drawing", command=start_drawing, bg="green", fg="white", width=15).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Exit", command=root.quit, bg="red", fg="white", width=10).grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

# Entry point
if __name__ == "__main__":
    launch_gui()