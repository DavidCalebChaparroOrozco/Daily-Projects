# Import necessary libraries
import tkinter as tk
from tkinter import messagebox, ttk
import threading
import csv
from PIL import Image, ImageTk

class BasketballShotClockGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Basketball Shot Clock by David Caleb")
        self.root.configure(bg="#1F1F1F")  
        self.shot_clock_time = 24
        self.is_running = False
        self.players = {}  # Dictionary to store player scores

        # Custom style for buttons
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12), background="#4CAF50", foreground="#000000")  
        self.style.map("TButton", background=[("active", "#45A049")])  

        # GUI Elements
        self.time_label = tk.Label(root, text="24", font=("Arial", 48), bg="#1F1F1F", fg="#FFFFFF")  
        self.time_label.pack(pady=20)

        # Frame for buttons
        self.button_frame = tk.Frame(root, bg="#1F1F1F")
        self.button_frame.pack(pady=10)

        self.start_button = ttk.Button(self.button_frame, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = ttk.Button(self.button_frame, text="Pause", command=self.pause)
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = ttk.Button(self.button_frame, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.save_button = ttk.Button(self.button_frame, text="Save Stats", command=self.save_stats)
        self.save_button.pack(side=tk.LEFT, padx=10)

        # Frame for player inputs
        self.player_frame = tk.Frame(root, bg="#1F1F1F")
        self.player_frame.pack(pady=20)

        self.player_name_entry = ttk.Entry(self.player_frame, font=("Arial", 12))
        self.player_name_entry.pack(side=tk.LEFT, padx=5)

        self.add_player_button = ttk.Button(self.player_frame, text="Add Player", command=self.add_player)
        self.add_player_button.pack(side=tk.LEFT, padx=5)

        # Frame for player scores
        self.score_frame = tk.Frame(root, bg="#1F1F1F")
        self.score_frame.pack(pady=10)

        # Dictionary to store score labels
        self.score_labels = {}  

        # Canvas for clock animation
        self.canvas = tk.Canvas(root, width=200, height=200, bg="#1F1F1F", highlightthickness=0)
        self.canvas.pack(pady=10)
        self.clock_face = self.canvas.create_oval(10, 10, 190, 190, outline="#4CAF50", width=5)  

    def start(self):
        if not self.is_running:
            self.is_running = True
            threading.Thread(target=self.countdown).start()

    def pause(self):
        self.is_running = False

    def reset(self):
        self.is_running = False
        self.shot_clock_time = 24
        self.time_label.config(text="24")
        # Reset player scores
        self.players = {}  
        self.update_score_display()
        self.canvas.delete("progress")

    def countdown(self):
        while self.shot_clock_time > 0 and self.is_running:
            self.shot_clock_time -= 1
            self.time_label.config(text=str(self.shot_clock_time))
            self.update_clock_animation()
            self.root.update()
            # Wait for 1 second
            self.root.after(1000)  

        if self.shot_clock_time == 0:
            messagebox.showinfo("Time's up!", "Buzzer! Time's up!")
            self.is_running = False
            self.show_winner()

    def add_player(self):
        player_name = self.player_name_entry.get().strip()
        if player_name and player_name not in self.players:
            # Initialize player score to 0
            self.players[player_name] = 0  
            self.update_score_display()
            self.player_name_entry.delete(0, tk.END)

    def update_score_display(self):
        # Clear existing score labels
        for widget in self.score_frame.winfo_children():
            widget.destroy()

        # Add new score labels
        for player, score in self.players.items():
            label = tk.Label(self.score_frame, text=f"{player}: {score}", font=("Arial", 14), bg="#1F1F1F", fg="#FFFFFF")
            label.pack()
            self.score_labels[player] = label

            # Add buttons to increment scores
            increment_button = ttk.Button(self.score_frame, text=f"+1 {player}", command=lambda p=player: self.increment_score(p))
            increment_button.pack()

    def increment_score(self, player):
        if player in self.players:
            self.players[player] += 1
            self.update_score_display()

    def show_winner(self):
        if self.players:
            winner = max(self.players, key=self.players.get)
            if self.players[winner] >= 10:  # Desafío: 10 puntos
                messagebox.showinfo("Champion!", f"{winner} is the champion with {self.players[winner]} points!")
            else:
                messagebox.showinfo("Winner", f"The winner is {winner} with {self.players[winner]} points!")
        else:
            messagebox.showinfo("No Players", "No players were added to the competition.")

    def save_stats(self):
        with open("player_stats.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Player", "Score"])
            for player, score in self.players.items():
                writer.writerow([player, score])
        messagebox.showinfo("Stats Saved", "Player statistics have been saved to player_stats.csv.")

    def update_clock_animation(self):
        if self.is_running:
            progress = self.shot_clock_time / 24 
            self.canvas.delete("progress")
            self.canvas.create_arc(10, 10, 190, 190, start=90, extent=360 * progress, outline="#4CAF50", width=5, tags="progress")

if __name__ == "__main__":
    root = tk.Tk()
    app = BasketballShotClockGUI(root)
    root.mainloop()