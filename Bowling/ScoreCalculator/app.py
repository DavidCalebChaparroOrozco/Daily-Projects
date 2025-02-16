# Validate the input rolls to ensure they follow bowling rules.
def validate_rolls(rolls):
    """
    - 'X' represents a strike.
    - '/' represents a spare.
    - Numbers represent the number of pins knocked down.
    """
    for roll in rolls:
        if roll not in ['X', '/'] and not roll.isdigit():
            return False
        if roll.isdigit() and (int(roll) < 0 or int(roll) > 10):
            return False
    return True

# Calculate the total score of a bowling game based on the rolls.
def calculate_score(rolls):
    """
    - Strikes ('X') add 10 points plus the next two rolls.
    - Spares ('/') add 10 points plus the next roll.
    - Numbers add their face value.
    """
    score = 0
    frame_index = 0
    frames = []

    for frame in range(10):  # 10 frames in a game
        if frame_index >= len(rolls):
            break

        first_roll = rolls[frame_index]

        # Handle Strike
        if first_roll == 'X':
            score += 10
            # Add the next two rolls for a strike
            if frame_index + 1 < len(rolls):
                score += get_roll_value(rolls[frame_index + 1])
            if frame_index + 2 < len(rolls):
                score += get_roll_value(rolls[frame_index + 2])
            frame_index += 1
            frames.append(['X', ' '])  # Mark strike in the frame

        # Handle Spare or Normal Frame
        else:
            second_roll = rolls[frame_index + 1] if frame_index + 1 < len(rolls) else '0'
            if second_roll == '/':
                score += 10
                # Add the next roll for a spare
                if frame_index + 2 < len(rolls):
                    score += get_roll_value(rolls[frame_index + 2])
                frames.append([first_roll, '/'])
            else:
                score += get_roll_value(first_roll) + get_roll_value(second_roll)
                frames.append([first_roll, second_roll])
            frame_index += 2

    return score, frames

# Get the numeric value of a roll.
def get_roll_value(roll):
    """
    - 'X' or '/' is worth 10.
    - Numbers are worth their face value.
    """
    if roll in ['X', '/']:
        return 10
    return int(roll)

# Display the scorecard in a table format.
def display_scorecard(frames, total_score):
    print("\n--- Bowling Scorecard ---")
    print("Frame | Roll 1 | Roll 2 | Cumulative Score")
    print("=".center(50,"="))
    cumulative_score = 0

    for i, frame in enumerate(frames):
        # Calculate cumulative score for the current frame
        if frame[0] == 'X':
            cumulative_score += 10
        elif frame[1] == '/':
            cumulative_score += 10
        else:
            cumulative_score += get_roll_value(frame[0]) + get_roll_value(frame[1])
        print(f"{i + 1:5} | {frame[0]:6} | {frame[1]:6} | {cumulative_score:15}")
    print("=".center(50,"="))
    print(f"Total Score: {total_score}\n")

# Main function to run the bowling score calculator.
def main():
    print("Welcome to the Bowling Score Calculator!")
    print("Enter the rolls for each frame. Use 'X' for a strike, '/' for a spare, or numbers for pins knocked down.")

    # Input rolls
    rolls = []
    while True:
        roll = input(f"Enter roll #{len(rolls) + 1} (or 'done' to finish): ").strip().upper()
        if roll == 'DONE':
            break
        rolls.append(roll)

    # Validate rolls
    if not validate_rolls(rolls):
        print("Invalid input. Please ensure rolls follow bowling rules.")
        return

    # Calculate score and display scorecard
    total_score, frames = calculate_score(rolls)
    display_scorecard(frames, total_score)

if __name__ == "__main__":
    main()