# Import necessary libraries
import itertools
import time
from typing import List, Dict
import matplotlib.pyplot as plt
import sys

# Initialize the CatNapper with default nap duration options.
class CatNapper:
    def __init__(self):
        # in hours
        self.possible_nap_durations = [3, 4, 6, 2]  
        # total sleep time in hours
        self.target_sleep = 12  
        self.all_combinations = []
        self.calculated = False

    # Calculate all possible combinations of naps that sum to exactly 12 hours.
    # Uses a recursive approach to find all valid combinations.
    def calculate_combinations(self):
        if self.calculated:
            return
            
        print("\n🐱 Calculating all possible nap combinations...")
        start_time = time.time()
        
        # We'll find combinations with up to 24 naps (since 12/0.5 = 24)
        max_naps = int(self.target_sleep / min(self.possible_nap_durations))
        
        # Find all combinations
        self.all_combinations = []
        for r in range(1, max_naps + 1):
            for combo in itertools.product(self.possible_nap_durations, repeat=r):
                if sum(combo) == self.target_sleep:
                    self.all_combinations.append(combo)
        
        # Remove duplicate combinations that are just reordered
        unique_combinations = set(tuple(sorted(combo)) for combo in self.all_combinations)
        self.all_combinations = [list(combo) for combo in unique_combinations]
        
        # Sort by number of naps
        self.all_combinations.sort(key=lambda x: len(x))
        
        end_time = time.time()
        print(f"✅ Found {len(self.all_combinations)} unique nap combinations in {end_time-start_time:.2f} seconds!")
        self.calculated = True

    # Return statistics about the nap combinations
    def get_stats(self) -> Dict:
        if not self.calculated:
            self.calculate_combinations()
            
        stats = {
            'total_combinations': len(self.all_combinations),
            'min_naps': len(self.all_combinations[0]) if self.all_combinations else 0,
            'max_naps': len(self.all_combinations[-1]) if self.all_combinations else 0,
            'most_common_duration': self._get_most_common_duration(),
            'average_naps_per_combo': sum(len(combo) for combo in self.all_combinations) / len(self.all_combinations)
        }
        return stats

    # Helper method to find the most common nap duration across all combinations
    def _get_most_common_duration(self) -> float:
        duration_counts = {}
        for combo in self.all_combinations:
            for duration in combo:
                duration_counts[duration] = duration_counts.get(duration, 0) + 1
        
        return max(duration_counts.items(), key=lambda x: x[1])[0]

    # Display a sample of nap combinations
    def display_combinations(self, num_to_display: int = 5):
        if not self.calculated:
            self.calculate_combinations()
            
        print(f"\n🐾 Sample of {num_to_display} nap combinations (out of {len(self.all_combinations)}):")
        for i, combo in enumerate(self.all_combinations[:num_to_display]):
            print(f"{i+1}. {len(combo)} naps: {', '.join(str(d) for d in combo)}")
        
        if len(self.all_combinations) > num_to_display:
            print("\n... and many more! Use 'show all' to see everything.")

    # Create visualizations of the nap combinations
    def visualize_combinations(self):
        if not self.calculated:
            self.calculate_combinations()
            
        print("\n📊 Creating visualizations...")
        
        # Prepare data for visualization
        nap_counts = [len(combo) for combo in self.all_combinations]
        duration_distribution = {}
        
        for combo in self.all_combinations:
            for duration in combo:
                duration_distribution[duration] = duration_distribution.get(duration, 0) + 1

        # Plot 1: Distribution of number of naps per combination
        plt.figure(figsize=(12, 5))
        plt.subplot(1, 2, 1)
        plt.hist(nap_counts, bins=range(min(nap_counts), max(nap_counts)+1), edgecolor='black')
        plt.title('Distribution of Number of Naps per Combination')
        plt.xlabel('Number of Naps')
        plt.ylabel('Frequency')
        plt.grid(True, linestyle='--', alpha=0.7)

        # Plot 2: Distribution of nap durations
        plt.subplot(1, 2, 2)
        durations = list(duration_distribution.keys())
        counts = list(duration_distribution.values())
        plt.bar([str(d) for d in durations], counts, color='orange')
        plt.title('Frequency of Each Nap Duration')
        plt.xlabel('Nap Duration (hours)')
        plt.ylabel('Count')
        plt.grid(True, linestyle='--', alpha=0.7)

        plt.tight_layout()
        plt.show()

    # Find all combinations that use exactly the specified number of naps
    def find_combinations_by_naps(self, num_naps: int) -> List[List[float]]:
        if not self.calculated:
            self.calculate_combinations()
            
        return [combo for combo in self.all_combinations if len(combo) == num_naps]

    # Save all combinations to a text file
    def save_combinations_to_file(self, filename: str = "cat_nap_combinations.txt"):
        if not self.calculated:
            self.calculate_combinations()
            
        try:
            with open(filename, 'w') as f:
                f.write(f"All possible nap combinations totaling {self.target_sleep} hours:\n\n")
                for i, combo in enumerate(self.all_combinations, 1):
                    f.write(f"{i}. {len(combo)} naps: {', '.join(str(d) for d in combo)}\n")
            print(f"\n💾 All combinations saved to {filename}!")
        except Exception as e:
            print(f"\n❌ Error saving file: {e}")

# Display the main menu options
def display_menu():
    print("\n" + "="*50)
    print("🐱 CATNAPPER: SLEEP COMBINATIONS CALCULATOR by DAVID CALEB".center(50))
    print("=".center(50, '='))
    print("1. Calculate all nap combinations")
    print("2. Show statistics")
    print("3. Display sample combinations")
    print("4. Find combinations by number of naps")
    print("5. Visualize combinations")
    print("6. Save combinations to file")
    print("7. Change nap duration options")
    print("8. Exit")
    print("=".center(50, '='))

# Get validated user input for menu choices
def get_user_choice(prompt: str, min_val: int, max_val: int) -> int:
    while True:
        try:
            choice = int(input(prompt))
            if min_val <= choice <= max_val:
                return choice
            print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    cat_napper = CatNapper()
    
    print("\nWelcome to CatNapper! 😺")
    print("This program calculates all possible ways your cat can nap")
    print(f"throughout the day to sleep exactly {cat_napper.target_sleep} hours.")
    
    while True:
        display_menu()
        choice = get_user_choice("Enter your choice (1-8): ", 1, 8)
        
        if choice == 1:
            cat_napper.calculate_combinations()
        elif choice == 2:
            if not cat_napper.calculated:
                print("\n⚠ Please calculate combinations first (option 1).")
                continue
            stats = cat_napper.get_stats()
            print("\n📈 Nap Combination Statistics:")
            print(f"Total unique combinations: {stats['total_combinations']}")
            print(f"Minimum naps needed: {stats['min_naps']}")
            print(f"Maximum naps in any combination: {stats['max_naps']}")
            print(f"Most common nap duration: {stats['most_common_duration']} hours")
            print(f"Average naps per combination: {stats['average_naps_per_combo']:.1f}")
        elif choice == 3:
            if not cat_napper.calculated:
                print("\n⚠ Please calculate combinations first (option 1).")
                continue
            num_to_show = get_user_choice("\nHow many combinations to display? (1-50): ", 1, 50)
            cat_napper.display_combinations(num_to_show)
        elif choice == 4:
            if not cat_napper.calculated:
                print("\n⚠ Please calculate combinations first (option 1).")
                continue
            min_naps = cat_napper.get_stats()['min_naps']
            max_naps = cat_napper.get_stats()['max_naps']
            num_naps = get_user_choice(
                f"\nEnter number of naps to find combinations for ({min_naps}-{max_naps}): ", 
                min_naps, max_naps
            )
            combinations = cat_napper.find_combinations_by_naps(num_naps)
            print(f"\nFound {len(combinations)} combinations with {num_naps} naps:")
            for i, combo in enumerate(combinations[:10], 1):
                print(f"{i}. {', '.join(str(d) for d in combo)}")
            if len(combinations) > 10:
                print(f"... and {len(combinations)-10} more.")
        elif choice == 5:
            if not cat_napper.calculated:
                print("\n⚠ Please calculate combinations first (option 1).")
                continue
            cat_napper.visualize_combinations()
        elif choice == 6:
            if not cat_napper.calculated:
                print("\n⚠ Please calculate combinations first (option 1).")
                continue
            filename = input("\nEnter filename to save (default: cat_nap_combinations.txt): ")
            if not filename:
                filename = "cat_nap_combinations.txt"
            cat_napper.save_combinations_to_file(filename)
        elif choice == 7:
            print("\nCurrent nap duration options:", cat_napper.possible_nap_durations)
            new_durations = input("Enter new durations (comma-separated, e.g., '0.5,1,2,3'): ")
            try:
                new_durations = [float(d.strip()) for d in new_durations.split(',')]
                if any(d <= 0 for d in new_durations):
                    print("All durations must be positive numbers.")
                    continue
                cat_napper.possible_nap_durations = sorted(new_durations)
                cat_napper.calculated = False  # Need to recalculate
                print("Nap durations updated! Recalculate combinations to see changes.")
            except ValueError:
                print("Invalid input. Please enter numbers separated by commas.")
        elif choice == 8:
            print("\nThank you for using CatNapper! 😽 Goodbye!")
            sys.exit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user. Goodbye!")
        sys.exit()

# 5, 4, 3, 6, 1