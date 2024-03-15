import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage

class PomodoroTimer:
    def __init__(self):
        # Initialize the Tkinter application window
        self.root = tk.Tk()
        self.root.geometry("600x300")
        self.root.title("Pomodoro Timer")
        self.root.tk.call("wm", "iconphoto",self.root._w, PhotoImage(file="coffee.png"))

        # Configure styles for tabs and buttons
        self.s = ttk.Style()
        self.s.configure("TNotebook.Tab", font=("Ubuntu",16))
        self.s.configure("TButton", font=("Ubuntu",16))

        # Create a notebook for tabs
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", pady=10, expand=True)

        # Create tabs for Pomodoro, Short Break, and Long Break
        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)

        # Labels to display timer values
        self.pomodoro_timer_label = ttk.Label(self.tab1, text="25:00", font=("Ubuntu",48))
        self.pomodoro_timer_label.pack(pady=20)
        self.short_break_timer_label = ttk.Label(self.tab2, text="05:00", font=("Ubuntu",48))
        self.short_break_timer_label.pack(pady=20)
        self.long_break_timer_label = ttk.Label(self.tab3, text="15:00", font=("Ubuntu",48))
        self.long_break_timer_label.pack(pady=20)

        # Add tabs to the notebook
        self.tabs.add(self.tab1, text="Pomodoro")
        self.tabs.add(self.tab2, text="Short Break")
        self.tabs.add(self.tab3, text="Long Break")

        # Create a grid layout for buttons
        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(pady=10)

        # Buttons for control
        self.start_button = ttk.Button(self.grid_layout, text="Start", command=self.start_timer_thread)
        self.start_button.grid(row=0, column=0)
        self.skip_button = ttk.Button(self.grid_layout, text="Skip", command=self.skip_clock)
        self.skip_button.grid(row=0, column=1)
        self.reset_button = ttk.Button(self.grid_layout, text="Reset", command=self.reset_button)
        self.reset_button.grid(row=0, column=2)

        # Label to display Pomodoro count
        self.pomodoro_counter_label = ttk.Label(self.grid_layout, text="Pomodoros: 0", font=("Ubuntu",16))
        self.pomodoro_counter_label.grid(row=1, column=0, columnspan=3, pady=10)

        # Initialize variables
        self.pomodoros = 0
        self.skipped = False
        self.stopped = False
        self.running = False

        # Start the Tkinter event loop
        self.root.mainloop()

    def start_timer_thread(self):
        # Start timer thread
        if not self.running:
            timer = threading.Thread(target=self.start_timer)
            timer.start()
            self.running = True
    
    def start_timer(self):
        # Function to start the timer based on selected tab
        self.stopped = False
        self.skipped = False
        timer_id = self.tabs.index(self.tabs.select()) + 1

        if timer_id == 1:  # Pomodoro timer
            full_seconds = 60 * 25
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.pomodoro_timer_label.configure(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped or self.skipped:
                self.pomodoros += 1
                self.pomodoro_counter_label.config(text=f"Pomodoros: {self.pomodoros}")
                if self.pomodoros % 4 == 0:
                    self.tabs.select(2)  # Switch to long break
                else: 
                    self.tabs.select(1)  # Switch to short break
                self.start_timer()
        elif timer_id == 2:  # Short break timer
            full_seconds = 60 * 5
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.short_break_timer_label.configure(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped or self.skipped:
                self.tabs.select(0)  # Switch back to Pomodoro
                self.start_timer()
        elif timer_id == 3:  # Long break timer
            full_seconds = 60 * 15
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.long_break_timer_label.configure(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped or self.skipped:
                self.tabs.select(0)  # Switch back to Pomodoro
                self.start_timer()
        else:
            print("Invalid timer id")

    def reset_button(self):
        # Reset button action
        self.stopped = True
        self.skipped = False
        self.pomodoros = 0
        self.pomodoro_timer_label.config(text="25:00")
        self.short_break_timer_label.config(text="05:00")
        self.long_break_timer_label.config(text="15:00")
        self.pomodoro_counter_label.config(text="Pomodoros: 0")
        self.running = False

    def skip_clock(self):
        # Skip button action
        current_tab = self.tabs.index(self.tabs.select())
        if current_tab == 0:
            self.pomodoro_timer_label.config(text="25:00")
        elif current_tab == 1:
            self.short_break_timer_label.config(text="05:00")
        elif current_tab == 2:
            self.long_break_timer_label.config(text="15:00")
        
        self.stopped = True
        self.skipped = True

# Create an instance of the PomodoroTimer class to start the application
PomodoroTimer()
