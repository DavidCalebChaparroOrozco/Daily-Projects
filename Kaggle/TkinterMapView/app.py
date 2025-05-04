# Importing necessary libraries
from tkinter import *
import tkintermapview
from tkinter import ttk
from PIL import Image, ImageTk

# Create the root window
root = Tk()
root.title('David Caleb - Tkinter MapView')
root.geometry("900x800")

# Load the image
root.tk.call("wm", "iconphoto", root._w, PhotoImage(file="map.png"))

# Function to perform address lookup
def lookup():
    map_widget.set_address(my_entry.get())
    my_slider.config(value=9)

# Function to adjust map zoom based on slider value
def slide(e):
    map_widget.set_zoom(my_slider.get())

# Create a label frame for the map widget
my_label = LabelFrame(root)
my_label.pack(pady=20)

# Create a TkinterMapView widget for displaying maps
map_widget = tkintermapview.TkinterMapView(my_label, width=800, height=600, corner_radius=0)

# Set initial address for the map
map_widget.set_address("Museo del Agua, Medellin, Colombia")

# Set initial zoom level for the map
map_widget.set_zoom(20)

# Pack the map widget
map_widget.pack()

# Create a frame for input elements
my_frame = LabelFrame(root)
my_frame.pack(pady=10)

# Create an entry widget for entering address
my_entry = Entry(my_frame, font=("Helvetica", 28))
my_entry.grid(row=0, column=0, pady=20, padx=10)

# Create a button to trigger address lookup
my_button = Button(my_frame, text="Lookup", font=("Helvetica", 18), command=lookup)
my_button.grid(row=0, column=1, padx=10)

# Create a slider widget for adjusting map zoom
my_slider = ttk.Scale(my_frame, from_=4, to=20, orient=HORIZONTAL, command=slide, value=20, length=220)
my_slider.grid(row=0, column=2, padx=10)

# Start the Tkinter event loop
root.mainloop()
