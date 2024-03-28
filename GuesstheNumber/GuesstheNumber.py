# Importing necessary libraries
import tkinter as tk
from tkinter import PhotoImage, messagebox
import random

# Initialize the number of attempts and generate a random number as the answer
attempts = 10
answer = random.randint(1, 99)

# Function to check the user's answer
def check_answer(event=None):
    """Function to check the user's answer."""
    # Access global variables for attempts and text
    global attempts, text
    # Get the user's input from the entry widget
    guess = entry.get()
    # Check if the input is a digit
    if guess.isdigit():
        # Decrease the number of attempts
        attempts -= 1
        # Convert the input to an integer
        guess = int(guess)
        if answer == guess:
            text.set("You win! Congrats!!")
            # Hide the check button after winning
            btn_check.pack_forget()
            messagebox.showinfo("Congratulations!", "You've guessed the correct number!")
        elif attempts == 0:
            text.set("You are out of attempts. The correct number was: " + str(answer))
            # Hide the check button after running out of attempts
            btn_check.pack_forget()
            messagebox.showinfo("Game Over", "You are out of attempts. The correct number was: " + str(answer))
        else:
            hint = "Go Higher!" if guess < answer else "Go Lower!"
            text.set("Incorrect! You have " + str(attempts) + " attempts remaining - " + hint)
            messagebox.showinfo("Incorrect Guess", "Try Again! " + hint)
    else:
        # Set message for invalid input
        text.set("Invalid input! Please enter a number.")
        messagebox.showwarning("Invalid Input", "Please enter a valid number.")
    # Clear the entry widget after each attempt
    entry.delete(0, tk.END)
    return


# Create the main tkinter window
root = tk.Tk()
root.tk.call("wm", "iconphoto", root._w, PhotoImage(file="number.png"))

# Set the title of the window
root.title("Guess The Number by David Caleb")
# Set the dimensions of the window
root.geometry("500x150")

# Create a label widget
label = tk.Label(root, text="Guess the number between 1 & 99")  
label.pack()

# Create an entry widget for user input
entry = tk.Entry(root, width=50, borderwidth=6)
entry.pack()
# Bind the Enter key to the check_answer function
entry.bind('<Return>', check_answer)

# Create a button widget
btn_check = tk.Button(root, text="Check", command=check_answer)
btn_check.pack()

# Create a button to quit the application
btn_quit = tk.Button(root, text="Quit", command=root.destroy)  
btn_quit.pack()

# Create a StringVar to hold dynamic text
text = tk.StringVar()
text.set("You have 10 attempts remaining! Good Luck!")
# Create a label widget for dynamic text
guess_attempts = tk.Label(root, textvariable=text)
guess_attempts.pack()

root.mainloop()
