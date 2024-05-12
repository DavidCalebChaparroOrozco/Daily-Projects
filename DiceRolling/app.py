# Importing necessary libraries
import random

# Dictionary containing visual representations of the faces of a die.
DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

# Height and width of a die based on the visual representation of its faces.
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])

# Separator between die faces in the diagram.
DIE_FACE_SEPARATOR = " "

# Function to parse user input and convert it to an integer if it's between 1 and 6.
def parse_input(input_string):
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)

# Function to roll dice and return the results.
def roll_dice(num_dice):
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results

# Function to generate a diagram of the die faces and results.
def generate_dice_faces_diagram(dice_values):
    dice_faces = _get_dice_faces(dice_values)
    dice_faces_rows = _generate_dice_faces_rows(dice_faces)

    # Generate header with the word "RESULTS" centered.
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "=")

    # Concatenate all rows of the dice faces diagram.
    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram

# Internal function to get the visual representations of the die faces.
def _get_dice_faces(dice_values):
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])
    return dice_faces

# Internal function to generate rows of the dice faces diagram.
def _generate_dice_faces_rows(dice_faces):
    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)
    return dice_faces_rows

# Get and validate user's input
num_dice_input = input("How many dice do you want to roll? [1-6] ")
num_dice = parse_input(num_dice_input)

# Roll the dice
roll_results = roll_dice(num_dice)

# Generate the ASCII diagram of dice faces
dice_face_diagram = generate_dice_faces_diagram(roll_results)

# Display the diagram
print(f"\n{dice_face_diagram}")