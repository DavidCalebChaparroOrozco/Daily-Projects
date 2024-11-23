# Import necessary libraries
import random

# Define a class for the MusicGenerator
class MusicGenerator:
    def __init__(self):
        # Define the production rules for generating notes
        self.rules = {
            'A': ['A', 'B', 'C', 'D'],
            'B': ['E', 'F', 'G'],
            'C': ['A', 'B'],
            'D': ['C', 'E', 'F'],
            'E': ['G', 'A'],
            'F': ['A', 'B', 'C'],
            'G': ['D', 'E']
        }

    # Generate a melody starting from a given note and depth.
    def generate_melody(self, start_note, depth):
        """        
        start_note: The note to start generating from.
        depth: The number of recursive levels to generate.
        return: A string representing the generated melody.
        """
        if depth == 0:
            # Base case: return the starting note
            return start_note  
        
        # Get possible next notes based on the current note
        next_notes = self.rules.get(start_note, [])
        
        if not next_notes:
            # No further notes, return current note
            return start_note  
        
        # Randomly choose the next note and continue generating
        next_note = random.choice(next_notes)
        return start_note + " " + self.generate_melody(next_note, depth - 1)

# Main function to run the music generator
def main():
    generator = MusicGenerator()
    
    # Set the starting note and depth for melody generation
    starting_note = 'A'
    recursion_depth = 10
    
    # Generate and print the melody
    melody = generator.generate_melody(starting_note, recursion_depth)
    print("Generated Melody:", melody)

# Execute the main function
if __name__ == "__main__":
    main()