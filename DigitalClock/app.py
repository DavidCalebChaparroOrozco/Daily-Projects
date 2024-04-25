# Importing necessary libraries
from tkinter import *
from tkinter.ttk import *
from time import strftime

# creating tkinter window
root = Tk()
root.title('Clock by David Caleb')

# This function is used to display time on the label

def time():
	string = strftime('%H:%M:%S %p')
	lbl.config(text=string)
	lbl.after(1000, time)


# Styling the label widget so that clock will look more attractive
lbl = Label(root, font=('Arial', 40, 'bold'),
			background='blue',
			foreground='white')

# Placing clock at the centre of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()
