# Import necessary libraries
import random
import time
from typing import Optional

class BasketballTrainingRoulette:
    """
    A basketball training program that randomly selects exercises with additional features:
    - Exercise categories (shooting, conditioning, etc.)
    - Difficulty levels
    - Exercise history tracking
    - Customizable exercise lists
    - Session time tracking
    """
    def __init__(self):
        self.exercises = {
            'shooting': [
                {"name": "50 free throws", "difficulty": "medium"},
                {"name": "20 jump shots from the elbow", "difficulty": "medium"},
                {"name": "10 three-pointers from each corner", "difficulty": "hard"}
            ],
            'conditioning': [
                {"name": "5 full-court sprints", "difficulty": "hard"},
                {"name": "15 minutes of agility ladder", "difficulty": "medium"}
            ],
            'fundamentals': [
                {"name": "10 minutes of dribbling drills", "difficulty": "easy"},
                {"name": "15 layups with each hand", "difficulty": "easy"}
            ]
        }
        self.session_history = []
        self.session_start_time = None
        self.custom_exercises = []

    # Initialize a new training session
    def start_session(self):
        self.session_start_time = time.time()
        print("\n" + "="*50)
        print("Welcome to Basketball Training Roulette by David Caleb!".center(50))
        print("=".center(50, "="))
        print("\nI'll randomly select training exercises for you.")
        print("You can filter by category or difficulty if you want.\n")

    # Get a random exercise with optional filters
    def get_random_exercise(self, category: Optional[str] = None, difficulty: Optional[str] = None) -> dict:
        if category and category.lower() in self.exercises:
            pool = self.exercises[category.lower()]
        else:
            # Combine all exercises if no category specified
            pool = [ex for cat in self.exercises.values() for ex in cat]
        
        if difficulty:
            pool = [ex for ex in pool if ex["difficulty"] == difficulty.lower()]
        
        if not pool:
            return {"name": "No exercises match your criteria", "difficulty": "none"}
        
        return random.choice(pool)

    # Show available exercise categories
    def display_categories(self):
        print("\nAvailable Categories:")
        for i, category in enumerate(self.exercises.keys(), 1):
            print(f"{i}. {category.capitalize()}")
        print(f"{len(self.exercises)+1}. All Categories")

    # Allow user to add their own exercises
    def add_custom_exercise(self):
        print("\nAdd Custom Exercise")
        name = input("Exercise name: ")
        category = input("Category (shooting/conditioning/fundamentals): ")
        difficulty = input("Difficulty (easy/medium/hard): ")
        
        new_exercise = {
            "name": name,
            "difficulty": difficulty.lower()
        }
        
        if category.lower() in self.exercises:
            self.exercises[category.lower()].append(new_exercise)
        else:
            self.exercises[category.lower()] = [new_exercise]
        
        print(f"\nAdded '{name}' to {category} exercises!")

    # Display session history
    def show_history(self):
        if not self.session_history:
            print("\nNo exercises completed yet!")
            return
        
        print("\nSession History:")
        for i, ex in enumerate(self.session_history, 1):
            print(f"{i}. {ex['name']} ({ex['difficulty']})")

    # Conclude the training session
    def end_session(self):
        if self.session_start_time:
            duration = time.time() - self.session_start_time
            mins, secs = divmod(duration, 60)
            print(f"\nSession Duration: {int(mins)} minutes {int(secs)} seconds")
        
        print("\nExercises Completed:")
        self.show_history()
        print("\nGreat work! Keep improving your game!")
        print("=" * 50 + "\n")

    def main(self):
        self.start_session()
        
        while True:
            print("\n" + "-" * 50)
            print("MAIN MENU".center(50))
            print("=".center(50, "="))
            print("1. Get random exercise")
            print("2. Filter by category/difficulty")
            print("3. Add custom exercise")
            print("4. View session history")
            print("5. End session")
            
            choice = input("\nWhat would you like to do? (1-5): ")
            
            if choice == '1':
                exercise = self.get_random_exercise()
                print(f"\nYour exercise: {exercise['name']} ({exercise['difficulty']})")
                self.session_history.append(exercise)
            elif choice == '2':
                self.display_categories()
                cat_choice = input("\nChoose category (or press Enter for all): ")
                diff_choice = input("Choose difficulty (easy/medium/hard or press Enter): ")
                
                exercise = self.get_random_exercise(
                    category=cat_choice if cat_choice else None,
                    difficulty=diff_choice if diff_choice else None
                )
                print(f"\nYour exercise: {exercise['name']} ({exercise['difficulty']})")
                self.session_history.append(exercise)
            elif choice == '3':
                self.add_custom_exercise()
            elif choice == '4':
                self.show_history()
            elif choice == '5':
                self.end_session()
                break
            else:
                print("Invalid choice. Please enter 1-5.")

# main the program
if __name__ == "__main__":
    app = BasketballTrainingRoulette()
    app.main()