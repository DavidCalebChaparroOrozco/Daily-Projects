import random
from playerPositions import POSITION_EXERCISES

# Class responsible for generating basketball warm-up routines
class WarmUpRoutineGenerator:
    def __init__(self):
        # Base exercises common to all positions
        self.base_exercises = [
            {"name": "Light Jogging", "duration": 5, "intensity": "Low"},
            {"name": "Dynamic Stretching", "duration": 10, "intensity": "Medium"},
            {"name": "Jumping Jacks", "duration": 3, "intensity": "High"}
        ]

    # Generate a warm-up routine based on player position
    def generate_routine(self, position):
        """
        
        Args:
            position (str): Player's basketball position
        
        Returns:
            list: Customized warm-up routine
        """
        # Start with base exercises
        routine = self.base_exercises.copy()
        
        # Add position-specific exercises
        position_exercises = POSITION_EXERCISES.get(position, [])
        routine.extend(random.sample(position_exercises, min(3, len(position_exercises))))
        
        return routine

    # Display the generated warm-up routine
    def display_routine(self, routine):
        """        
        Args:
            routine (list): List of exercises
        """
        total_time = 0
        for exercise in routine:
            print(f"- {exercise['name']} ({exercise['duration']} mins, {exercise['intensity']} Intensity)")
            total_time += exercise['duration']
        
        print(f"\nTotal Warm-Up Time: {total_time} minutes")
