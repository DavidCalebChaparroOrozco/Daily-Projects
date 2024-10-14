# Importing necessary libraries
import tkinter as tk
from tkinter import ttk, messagebox

class BowlingScoreboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bowling Scoreboard by David Caleb")
        self.root.geometry("650x400")
        self.root.configure(bg="#2E2E2E")  # Dark background for the main window

        self.players = []
        self.scores = {}
        self.current_player = 0

        # Frame for input controls (add player, reset, etc.)
        self.control_frame = ttk.Frame(self.root, padding="10", style="ControlFrame.TFrame")
        self.control_frame.grid(row=0, column=0, padx=10, pady=10)

        # Entry for player name
        self.player_name_label = ttk.Label(self.control_frame, text="Player Name:", font=('Arial', 12), background="#2E2E2E", foreground="white")
        self.player_name_label.grid(row=0, column=0, sticky=tk.W)

        self.player_name_entry = ttk.Entry(self.control_frame, width=30)
        self.player_name_entry.grid(row=0, column=1, padx=10)

        # Button to add player
        self.add_player_button = ttk.Button(self.control_frame, text="Add Player", command=self.add_player)
        self.add_player_button.grid(row=0, column=2)

        # Button to reset the scoreboard
        self.reset_button = ttk.Button(self.control_frame, text="Reset", command=self.reset_scoreboard)
        self.reset_button.grid(row=0, column=3, padx=5)

        # Scoreboard frame
        self.scoreboard_frame = ttk.Frame(self.root, padding="10", style="ScoreboardFrame.TFrame")
        self.scoreboard_frame.grid(row=1, column=0, padx=10, pady=10)

        # Initialize scoreboard
        self.create_blank_scoreboard()

    # Adds a new player and creates their scoreboard.
    def add_player(self):
        player_name = self.player_name_entry.get().strip()
        if not player_name:
            messagebox.showerror("Error", "Please enter a valid player name.")
            return

        if player_name in self.players:
            messagebox.showerror("Error", "Player already exists.")
            return

        self.players.append(player_name)
        self.scores[player_name] = [[None, None] for _ in range(10)]  # Empty score data for 10 frames
        self.create_blank_scoreboard()

    # Creates a blank scoreboard for all players.
    def create_blank_scoreboard(self):
        for widget in self.scoreboard_frame.winfo_children():
            widget.destroy()

        for idx, player in enumerate(self.players):
            player_label = ttk.Label(self.scoreboard_frame, text=player, font=('Arial', 12, 'bold'), background="#2E2E2E", foreground="white")
            player_label.grid(row=idx * 4 + 1, column=0, pady=5)

            for frame in range(10):  # Create 10 frames for each player
                frame_label = ttk.Label(self.scoreboard_frame, text=f'Frame {frame+1}', font=('Arial', 10), background="#2E2E2E", foreground="white")
                frame_label.grid(row=0, column=frame+1)

                roll1_entry = ttk.Entry(self.scoreboard_frame, width=5, validate="key", 
                                        validatecommand=(self.root.register(self.validate_score), '%P'))
                roll1_entry.grid(row=idx * 4 + 1, column=frame + 1, padx=5)
                roll1_entry.bind('<FocusOut>', lambda e, p=player, f=frame, r=0: self.on_focus_out(e, p, f, r))

                roll2_entry = ttk.Entry(self.scoreboard_frame, width=5, validate="key", 
                                        validatecommand=(self.root.register(self.validate_score), '%P'))
                roll2_entry.grid(row=idx * 4 + 2, column=frame + 1, padx=5)
                roll2_entry.bind('<FocusOut>', lambda e, p=player, f=frame, r=1: self.on_focus_out(e, p, f, r))

                total_entry = ttk.Entry(self.scoreboard_frame, width=5)
                total_entry.grid(row=idx * 4 + 3, column=frame + 1, padx=5)
                total_entry.config(state=tk.DISABLED)

    # Validates that the score entered is numeric and between 0-9 (or 10 for a strike).
    def validate_score(self, value):
        if value.isdigit() and 0 <= int(value) <= 10:
            return True
        return False

    # Handles score input validation and dynamic navigation to the next input.
    def on_focus_out(self, event, player, frame, roll):
        entry = event.widget
        score = entry.get()

        if not score.isdigit() or not (0 <= int(score) <= 10):
            entry.delete(0, tk.END)
            messagebox.showerror("Invalid Score", "Please enter a valid score (0-10).")
            return

        score = int(score)
        self.scores[player][frame][roll] = score

        # Automatically move to the next entry if valid
        if roll == 0:
            if score == 10:  # Strike
                self.scores[player][frame][1] = 0  # Set second roll to 0 automatically
            else:
                self.focus_next_entry(event.widget, player, frame, roll + 1)
        else:
            self.calculate_total_score(player)
            if frame < 9:
                self.focus_next_entry(event.widget, player, frame + 1, 0)

    # Focuses on the next entry after valid input.
    def focus_next_entry(self, current_widget, player, next_frame, next_roll):
        for widget in self.scoreboard_frame.winfo_children():
            info = widget.grid_info()
            if info["row"] == self.players.index(player) * 4 + next_roll + 1 and info["column"] == next_frame + 1:
                widget.focus()
                break

    # Calculates the total score per frame while accounting for strikes and spares.
    def calculate_total_score(self, player):
        total = 0
        for frame in range(10):
            roll1, roll2 = self.scores[player][frame]

            if roll1 is None or roll2 is None:
                break  # Stop calculation if incomplete

            # Check for strike
            if roll1 == 10:
                total += 10 + (self.strike_bonus(player, frame) or 0)  
            # Check for spare
            elif roll1 + roll2 == 10:
                total += 10 + (self.spare_bonus(player, frame) or 0)  
            else:
                total += roll1 + roll2

            # Update the total score in the scoreboard
            self.update_total_entry(player, frame, total)

    # Calculates the bonus for a strike (next two rolls).
    def strike_bonus(self, player, frame):
        if frame >= 9:
            return 0  
        
        next_frame = self.scores[player][frame + 1]
        
        if next_frame[0] is None:  
            return 0
        
        if next_frame[0] == 10 and frame < 8:  
            next_next_frame = self.scores[player][frame + 2]
            return (10 + (next_next_frame[0] or 0)) if next_next_frame[0] is not None else 0
        
        return sum([next_frame[0] or 0 , next_frame[1] or 0])

    # Calculates the bonus for a spare (next one roll).
    def spare_bonus(self ,player ,frame):
        if frame >=9:
            return 0 
        next_frame=self.scores[player][frame+1]
        return next_frame[0]if next_frame[0]is not None else 0 

    # Updates the total score entry field in the scoreboard.
    def update_total_entry(self ,player ,frame ,total):
        for widget in self.scoreboard_frame.winfo_children():
            info = widget.grid_info()
            if info["row"] == self.players.index(player) * 4 + 3 and info["column"] == frame + 1:
                widget.config(state=tk.NORMAL)
                widget.delete(0, tk.END)
                widget.insert(0, str(total))
                widget.config(state=tk.DISABLED)

    # Resets the scoreboard ,removing all players and resetting the layout.
    def reset_scoreboard(self):
        self.players.clear()
        self.scores.clear()
        self.create_blank_scoreboard()

# Main Tkinter window setup
root = tk.Tk()
style = ttk.Style()
style.configure("ControlFrame.TFrame", background="#3C3C3C") 
style.configure("ScoreboardFrame.TFrame", background="#3C3C3C") 

app = BowlingScoreboardApp(root)
root.mainloop()