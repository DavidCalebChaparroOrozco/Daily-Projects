# Import necessary libraries
import random

# Display the current state of the pins in a simple ASCII format
def display_pins(pins):
    print("\nCurrent Pins:")
    print(" ".join(str(i+1) for i in range(len(pins)) if pins[i]))
    print(" ".join(" " if pins[i] else "X" for i in range(len(pins))))

# Get player input for force and direction with validation
def get_player_input():
    while True:
        try:
            force = int(input("Enter force (1-5, where 5 is strongest): "))
            if 1 <= force <= 5:
                break
            print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            direction = int(input("Enter direction (1-3, 1=left, 2=center, 3=right): "))
            if 1 <= direction <= 3:
                break
            print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Please enter a valid number.")

    return force, direction

# Calculate which pins are knocked down based on force and direction
def calculate_hit(force, direction, pins):
    # Base probability of hitting increases with force
    base_hit_chance = 0.2 + (force * 0.15)
    
    # Direction affects which pins are more likely to be hit

    # Left bias
    if direction == 1:  
        weights = [0.7, 0.5, 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    # Right bias
    elif direction == 3:  
        weights = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3, 0.5, 0.7, 0.7]
    # Center bias
    else:  
        weights = [0.2, 0.3, 0.5, 0.7, 0.9, 0.9, 0.7, 0.5, 0.3, 0.2]
    
    # Adjust weights by force
    adjusted_weights = [w * (1 + (force * 0.1)) for w in weights]
    
    # Determine which pins are knocked down
    new_pins = []
    for i in range(10):
        # Only consider standing pins
        if pins[i]:  
            hit_prob = adjusted_weights[i] * base_hit_chance
            if random.random() < hit_prob:
                # Pin is knocked down
                new_pins.append(False)  
            else:
                # Pin remains standing
                new_pins.append(True)  
        else:
            # Already knocked down
            new_pins.append(False)  
    
    return new_pins

# Main game loop for the bowling game
def play_game():
    print("Welcome to Mini Bowling Arcade!")
    print("Try to knock down all 10 pins with your ball!")
    
    total_score = 0
    round_num = 1
    
    # 10 rounds in a standard bowling game
    while round_num <= 10:  
        print(f"\n Round {round_num} ")
        # Reset pins (all standing)
        pins = [True] * 10  
        attempts = 0
        round_score = 0
        
        # Maximum 2 attempts per round
        while attempts < 2 and any(pins):  
            display_pins(pins)
            print(f"\nAttempt {attempts + 1}")
            force, direction = get_player_input()
            
            pins = calculate_hit(force, direction, pins)
            knocked_down = pins.count(False) - (10 - sum(pins))
            round_score += knocked_down
            
            print(f"\nYou knocked down {knocked_down} pins!")
            attempts += 1
        
        total_score += round_score
        print(f"\nRound {round_num} complete! Score: {round_score}")
        print(f"Total score: {total_score}")
        round_num += 1
    
    print("\nGame Over!")
    print(f"Your final score: {total_score}")
    if total_score >= 100:
        print("Wow! Perfect game!")
    elif total_score >= 80:
        print("Great job! You're a bowling pro!")
    elif total_score >= 50:
        print("Good game! Keep practicing!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    play_game()