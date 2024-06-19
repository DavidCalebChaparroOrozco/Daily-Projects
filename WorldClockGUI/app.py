# Importing necessary libraries
from datetime import datetime
import pytz
from tkinter import *
import time

root = Tk()
root.geometry("1500x400")
root.tk.call("wm", "iconphoto", root._w, PhotoImage(file="time_zone.png"))
root.title("World Clock GUI by David Caleb")

# Updates the time for a specific timezone and configures the clock and name labels.
def update_time(zone, clock, name_label, location):
    """
    Args:
    zone (str): The timezone to be updated.
    clock (Label): The Label widget displaying the time.
    name_label (Label): The Label widget displaying the location name.
    location (str): The name of the location.
    """
    home = pytz.timezone(zone)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%a %H:%M:%S")
    clock.config(text=current_time)
    name_label.config(text=location)
    clock.after(200, lambda: update_time(zone, clock, name_label, location))

# Initializes and updates the time for all specified timezones.
def times():
    timezones = [
        ("America/Bogota", clock1, name1, "Colombian"),
        ("America/New_York", clock2, name2, "New York"),
        ("Asia/Shanghai", clock3, name3, "China"),
        ("Europe/Berlin", clock4, name4, "Germany"),
        ("Europe/Oslo", clock5, name5, "Norway"),
    ]
    for zone, clock, name_label, location in timezones:
        update_time(zone, clock, name_label, location)

# Colombian time zone
f = Frame(root, bd=5)
f.place(x=10, y=118, width=220, height=150)
name1 = Label(f, font=("Trebuchet MS", 25, "bold"))
name1.place(x=50, y=10)

logo = PhotoImage(file="co.png")
image_label = Label(root, image=logo)
image_label.place(x=25, y=145)

clock1 = Label(f, font=("Trebuchet MS", 20))
clock1.place(x=5, y=80)

# USA time zone
f2 = Frame(root, bd=5)
f2.place(x=300, y=118, width=220, height=150)
name2 = Label(f2, font=("Trebuchet MS", 25, "bold"))
name2.place(x=30, y=10)

logo2 = PhotoImage(file="us.png")
image_label2 = Label(root, image=logo2)
image_label2.place(x=290, y=145)

clock2 = Label(f2, font=("Trebuchet MS", 20))
clock2.place(x=5, y=80)

# China time zone
f3 = Frame(root, bd=5)
f3.place(x=600, y=118, width=220, height=150)
name3 = Label(f3, font=("Trebuchet MS", 25, "bold"))
name3.place(x=50, y=10)

logo3 = PhotoImage(file="cn.png")
image_label3 = Label(root, image=logo3)
image_label3.place(x=600, y=145)

clock3 = Label(f3, font=("Trebuchet MS", 20))
clock3.place(x=5, y=80)

# German time zone
f4 = Frame(root, bd=5)
f4.place(x=900, y=118, width=220, height=150)
name4 = Label(f4, font=("Trebuchet MS", 25, "bold"))
name4.place(x=50, y=10)

logo4 = PhotoImage(file="de.png")
image_label4 = Label(root, image=logo4)
image_label4.place(x=900, y=145)

clock4 = Label(f4, font=("Trebuchet MS", 20))
clock4.place(x=5, y=80)

# Norway time zone
f5 = Frame(root, bd=5)
f5.place(x=1200, y=118, width=220, height=150)
name5 = Label(f5, font=("Trebuchet MS", 25, "bold"))
name5.place(x=50, y=10)

logo5 = PhotoImage(file="no.png")
image_label5 = Label(root, image=logo5)
image_label5.place(x=1200, y=145)

clock5 = Label(f5, font=("Trebuchet MS", 20))
clock5.place(x=5, y=80)

times()
root.mainloop()
