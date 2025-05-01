# Import necessary libraries
import random

# Validate if the input follows basic algebraic chess notation.
def is_valid_algebraic_notation(move):
    """
    Args:
        move: The chess move to validate
    Returns:
        bool: True if valid, False otherwise
    """
    if not move:
        return False
    
    # Basic validation for pawn moves (e4, dxe4, e8=Q, etc.)
    if len(move) >= 2:
        first_char = move[0]
        # Pawn move
        if first_char.islower():  
            # Check if it's a capture (contains 'x')
            if 'x' in move:
                parts = move.split('x')
                if len(parts) != 2:
                    return False
                file, rest = parts[0], parts[1]
                if len(file) != 1 or not file.islower():
                    return False
            # Check promotion
            if '=' in move:
                parts = move.split('=')
                if len(parts) != 2:
                    return False
                promotion_piece = parts[1]
                if promotion_piece not in ['Q', 'R', 'B', 'N']:
                    return False
            # Check basic move format (e4)
            if move[0].islower() and move[1].isdigit():
                return True
        # Piece moves (Nf3, Bxe5, Qd2, etc.)
        elif first_char.isupper() and first_char in ['K', 'Q', 'R', 'B', 'N']:
            return True
    
    return False

# Generate a random chess move in descriptive format.
def generate_random_move():
    """
    Returns:
        str: A move in format "e2 to e4"
    """
    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    start_file = random.choice(files)
    start_rank = random.randint(1, 8)
    end_file = random.choice(files)
    end_rank = random.randint(1, 8)
    
    return f"{start_file}{start_rank} to {end_file}{end_rank}"

# Convert descriptive move to algebraic notation (simplified version).
def descriptive_to_algebraic(descriptive_move):
    """
    Args:
        descriptive_move: Move in format "e2 to e4"
    Returns:
        str: Move in algebraic notation "e4"
    """
    parts = descriptive_move.split(' to ')
    if len(parts) == 2:
        return parts[1]
    return ""

# Main training function that presents moves and checks user answers.
def train_notation_conversion():
    print("Chess Notation Trainer by David Caleb")
    print("Type 'quit' to exit the trainer.\n")
    
    while True:
        # Randomly choose between showing descriptive or algebraic notation
        if random.choice([True, False]):
            # Show descriptive, ask for algebraic
            descriptive_move = generate_random_move()
            print(f"Descriptive: {descriptive_move}")
            user_input = input("Algebraic notation: ").strip()
            
            if user_input.lower() == 'quit':
                break
                
            correct_answer = descriptive_to_algebraic(descriptive_move)
            if user_input == correct_answer:
                print("Correct!\n")
            else:
                print(f"Incorrect. The correct answer is: {correct_answer}\n")
        else:
            # Show algebraic, ask for descriptive (simplified version)
            # For simplicity, we'll just use pawn moves here
            file = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
            rank = random.randint(1, 8)
            algebraic_move = f"{file}{rank}"
            print(f"Algebraic: {algebraic_move}")
            user_input = input("Descriptive notation (format 'e2 to e4'): ").strip()
            
            if user_input.lower() == 'quit':
                break
                
            correct_answer = f"{file}{rank-1} to {algebraic_move}"  # Simplification
            if user_input.lower() == correct_answer.lower():
                print("Correct!\n")
            else:
                print(f"Incorrect. The correct answer is: {correct_answer}\n")

if __name__ == "__main__":
    train_notation_conversion()