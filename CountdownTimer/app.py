# Importing necessary libraries
import tkinter as tk
from datetime import datetime, timedelta
import time
import pygame

# Initialize Pygame for sound effects
pygame.mixer.init()

# Load the celebration sound
pygame.mixer.music.load("sound.mp3")

class CountdownTimer:
    def __init__(self, master):
        self.master = master
        master.title("Countdown Timer to New Year by David Caleb")
        
        # Set the target time for New Year
        self.target_time = datetime(year=datetime.now().year + 1, month=1, day=1, hour=0, minute=0, second=0)

        master.configure(bg="Black")
        
        # Create label to display the countdown
        self.label = tk.Label(master, font=("Comic Sans MS", 48), fg="gold", bg="Black")
        self.label.pack(pady=20)

        # Start the countdown
        self.update_timer()
    
    def update_timer(self):
        # Calculate the remaining time until New Year
        now = datetime.now()
        remaining_time = self.target_time - now
        
        # If the countdown has reached zero, play sound and show message
        if remaining_time <= timedelta(0):
            self.label.config(text="Happy New Year!")
            pygame.mixer.music.play()
            return
        
        # Format the remaining time into hours, minutes, and seconds
        hours, remainder = divmod(int(remaining_time.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        
        # Update the label with the remaining time
        self.label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        
        # Call this method again after 1 second
        self.master.after(1000, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    countdown_timer = CountdownTimer(root)
    root.mainloop()
