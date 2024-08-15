# Importing necessary libraries
from tkinter import *
import random

# Initializing the main application window
class RockPaperScissorGame:
    def __init__(self, root):
        self.root = root
        # Set window title
        self.root.title("Rock Paper Scissor Game")  
        # Set window dimensions
        self.root.geometry("600x300")  
        # Disable window resizing
        self.root.resizable(False, False)  

        # Computer choices dictionary
        self.computer_choices = {
            "0": "Rock",
            "1": "Paper",
            "2": "Scissor"
        }

        # Creating and placing the game widgets
        self.create_widgets()

    # Function to create and place widgets on the screen
    def create_widgets(self):
        # Game Title
        Label(self.root, text="Rock Paper Scissor by David Caleb", font="normal 24 bold", fg="blue").pack(pady=20)

        # Frame for player and computer labels
        self.frame = Frame(self.root)
        self.frame.pack()

        # Player label
        self.player_label = Label(self.frame, text="Player", font=("Arial", 16))
        self.player_label.pack(side=LEFT)

        # VS label
        self.vs_label = Label(self.frame, text="VS", font=("Arial", 16, "bold"))
        self.vs_label.pack(side=LEFT, padx=20)

        # Computer label
        self.computer_label = Label(self.frame, text="Computer", font=("Arial", 16))
        self.computer_label.pack(side=LEFT)

        # Result label
        self.result_label = Label(self.root, text="", font=("Arial", 20, "bold"), bg="white", width=15, borderwidth=2, relief="solid")
        self.result_label.pack(pady=20)

        # Frame for action buttons (Rock, Paper, Scissor)
        self.button_frame = Frame(self.root)
        self.button_frame.pack()

        # Buttons for player choices
        self.rock_button = Button(self.button_frame, text="🪨", font=("Arial", 16), width=7, command=self.select_rock)
        self.rock_button.pack(side=LEFT, padx=10)

        self.paper_button = Button(self.button_frame, text="🗒️", font=("Arial", 16), width=7, command=self.select_paper)
        self.paper_button.pack(side=LEFT, padx=10)

        self.scissor_button = Button(self.button_frame, text="✂️", font=("Arial", 16), width=7, command=self.select_scissor)
        self.scissor_button.pack(side=LEFT, padx=10)

        # Reset Game Button
        self.reset_button = Button(self.root, text="Reset Game", font=("Arial", 14), fg="white", bg="green", command=self.reset_game)
        self.reset_button.pack(pady=20)

    # Function to reset the game to its initial state
    def reset_game(self):
        self.rock_button["state"] = "active"
        self.paper_button["state"] = "active"
        self.scissor_button["state"] = "active"
        self.player_label.config(text="Player")
        self.computer_label.config(text="Computer")
        self.result_label.config(text="")

    # Function to disable buttons after a choice is made
    def disable_buttons(self):
        self.rock_button["state"] = "disabled"
        self.paper_button["state"] = "disabled"
        self.scissor_button["state"] = "disabled"

    # Function to handle player's choice of Rock
    def select_rock(self):
        computer_choice = self.computer_choices[str(random.randint(0, 2))]
        if computer_choice == "Rock":
            result = "Match Draw"
        elif computer_choice == "Scissor":
            result = "Player Wins"
        else:
            result = "Computer Wins"
        self.display_result("Rock", computer_choice, result)

    # Function to handle player's choice of Paper
    def select_paper(self):
        computer_choice = self.computer_choices[str(random.randint(0, 2))]
        if computer_choice == "Paper":
            result = "Match Draw"
        elif computer_choice == "Scissor":
            result = "Computer Wins"
        else:
            result = "Player Wins"
        self.display_result("Paper", computer_choice, result)

    # Function to handle player's choice of Scissor
    def select_scissor(self):
        computer_choice = self.computer_choices[str(random.randint(0, 2))]
        if computer_choice == "Rock":
            result = "Computer Wins"
        elif computer_choice == "Scissor":
            result = "Match Draw"
        else:
            result = "Player Wins"
        self.display_result("Scissor", computer_choice, result)

    # Function to update the labels with the player and computer choices and the result
    def display_result(self, player_choice, computer_choice, result):
        self.player_label.config(text=player_choice)
        self.computer_label.config(text=computer_choice)
        self.result_label.config(text=result)
        self.disable_buttons()

# Main loop to run the application
if __name__ == "__main__":
    root = Tk()
    app = RockPaperScissorGame(root)
    root.mainloop()