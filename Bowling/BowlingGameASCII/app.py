# Importing necessary libraries
import random
import time

# Function to display the pins as ASCII art
def display_pins(pins):
    """
    Displays the current state of the bowling pins using ASCII.
    'O' represents a standing pin and ' ' represents a knocked-down pin.
    """
    pin_art = [
        [pins[6]],
        [pins[3], pins[7]],
        [pins[1], pins[4], pins[8]],
        [pins[0], pins[2], pins[5], pins[9]]
    ]
    print("Bowling Pins:")
    for row in pin_art:
        print("  " * (3 - len(row)) + "  ".join(row))
    print()

# Function to simulate the bowling roll
def roll_ball():
    """
    Simulates a ball roll and returns a list representing knocked-down pins.
    1 means the pin is knocked down, 0 means it is still standing.
    """
    return [random.choice([0, 1]) for _ in range(10)]

# Function to calculate the number of knocked-down pins
def calculate_score(pins):
    """
    Calculates the score of the current roll by counting the knocked-down pins.
    """
    return sum([1 for pin in pins if pin == " "])

# Function to reset the pins to their initial state
def reset_pins():
    """
    Resets the pins to their standing position represented by 'O'.
    """
    return ['O'] * 10

# Main bowling game function
def bowling_game():
    """
    Main function for the bowling game, allows the player to roll the ball,
    see the knocked-down pins, and gives options to restart or exit.
    """
    print("Welcome to the Console Bowling Game!")
    print("Try to knock down all the pins.")
    # Initialize pins
    pins = reset_pins()  
    # Number of rolls taken
    rolls = 0  
    # Total score
    total_score = 0  

    while True:
        print(f"Roll {rolls + 1}:")
        # Show the pins before the roll
        display_pins(pins)  

        # Simulate the ball roll and update the pins
        knocked_pins = roll_ball()
        for i in range(10):
            if knocked_pins[i] == 1:
                # Update knocked-down pins with space
                pins[i] = " "  

        # Show pins after the roll
        display_pins(pins)  
        score = calculate_score(pins)
        total_score += score
        print(f"You knocked down {score} pins this roll.")
        rolls += 1
        print(f"Total score: {total_score}\n")

        # Check if all pins are knocked down
        if all(pin == " " for pin in pins):
            print("Congratulations! All pins are down!")
            # Bonus points for knocking all pins
            total_score += 10  
            break

        # Ask the user if they want to continue or restart
        if rolls == 2:
            print("You've finished two rolls. Do you want to:")
            print("1. Play again")
            print("2. Exit")
            choice = input("Enter 1 or 2: ")
            if choice == "1":
                pins = reset_pins() 
                rolls = 0
                total_score = 0
                print("\nGame restarted!\n")
            elif choice == "2":
                print("Thank you for playing!")
                break
            else:
                print("Invalid input. Exiting the game.")
                break

# Run the game
if __name__ == "__main__":
    bowling_game()
