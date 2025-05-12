# Import necessary libraries
import json
import os
from typing import Dict, List, Optional

# Constants
DATA_FILE = "players_data.json"
MIN_JERSEY_NUMBER = 1
MAX_JERSEY_NUMBER = 99

# Class to represent a player with name and jersey number.
class Player:
    
    def __init__(self, name: str, jersey_number: int):
        self.name = name
        self.jersey_number = jersey_number
    
    # Convert Player object to dictionary for JSON serialization.
    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "jersey_number": self.jersey_number
        }
    
    @classmethod
    # Create Player object from dictionary.
    def from_dict(cls, data: Dict) -> 'Player':
        return cls(data["name"], data["jersey_number"])
    
    def __str__(self) -> str:
        return f"{self.name} (#{self.jersey_number})"

# Class to manage player database operations.
class PlayerManager:
    
    def __init__(self):
        self.players: List[Player] = []
        self.load_data()
    
    # Add a new player to the database after validation.
    def add_player(self, name: str, jersey_number: int) -> bool:
        if not self.validate_player(name, jersey_number):
            return False
        
        if self.get_player_by_number(jersey_number):
            print(f"Error: Jersey number #{jersey_number} is already taken.")
            return False
        
        self.players.append(Player(name, jersey_number))
        self.save_data()
        print(f"Successfully added {name} (#{jersey_number}) to the database.")
        return True
    
    # Validate player data before adding to database.
    def validate_player(self, name: str, jersey_number: int) -> bool:
        if not name.strip():
            print("Error: Player name cannot be empty.")
            return False
        
        if not MIN_JERSEY_NUMBER <= jersey_number <= MAX_JERSEY_NUMBER:
            print(f"Error: Jersey number must be between {MIN_JERSEY_NUMBER} and {MAX_JERSEY_NUMBER}.")
            return False
        
        return True
    
    # Search for player by name (case-insensitive partial match).
    def get_player_by_name(self, name: str) -> Optional[Player]:
        name_lower = name.lower()
        for player in self.players:
            if name_lower in player.name.lower():
                return player
        return None
    
    # Search for player by exact jersey number match.
    def get_player_by_number(self, jersey_number: int) -> Optional[Player]:
        for player in self.players:
            if player.jersey_number == jersey_number:
                return player
        return None
    
    # Display all players in the database.
    def list_players(self) -> None:
        if not self.players:
            print("No players in the database.")
            return
        
        print("\nCurrent Players:")
        print("=".center(50,"="))
        for player in sorted(self.players, key=lambda x: x.jersey_number):
            print(player)
        print("=".center(50,"="))
        print(f"Total players: {len(self.players)}\n")
    
    # Update player information.
    def update_player(self, old_number: int, new_name: str, new_number: int) -> bool:
        player = self.get_player_by_number(old_number)
        if not player:
            print(f"Error: No player found with jersey number #{old_number}.")
            return False
        
        if not self.validate_player(new_name, new_number):
            return False
        
        # Check if new number is available (unless it's the same number)
        if new_number != old_number and self.get_player_by_number(new_number):
            print(f"Error: Jersey number #{new_number} is already taken.")
            return False
        
        player.name = new_name
        player.jersey_number = new_number
        self.save_data()
        print(f"Successfully updated player to {new_name} (#{new_number}).")
        return True
    
    # Remove player from database by jersey number.
    def delete_player(self, jersey_number: int) -> bool:
        player = self.get_player_by_number(jersey_number)
        if not player:
            print(f"Error: No player found with jersey number #{jersey_number}.")
            return False
        
        self.players.remove(player)
        self.save_data()
        print(f"Successfully removed #{jersey_number} from the database.")
        return True
    
    # Save player data to JSON file.
    def save_data(self) -> None:
        data = [player.to_dict() for player in self.players]
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    
    # Load player data from JSON file.
    def load_data(self) -> None:
        if not os.path.exists(DATA_FILE):
            self.players = []
            return
        
        try:
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
                self.players = [Player.from_dict(item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError):
            print("Warning: Could not load player data. Starting with empty database.")
            self.players = []

# Display the main menu options.
def display_menu() -> None:
    print("\nPlayer Jersey Number Checker")
    print("=".center(50,"="))
    print("1. Add New Player")
    print("2. Search by Name")
    print("3. Search by Jersey Number")
    print("4. List All Players")
    print("5. Update Player Information")
    print("6. Delete Player")
    print("7. Exit")
    print("=".center(50,"="))

# Get validated integer input from user.
def get_int_input(prompt: str, min_val: int = None, max_val: int = None) -> int:
    while True:
        try:
            value = int(input(prompt))
            if (min_val is not None and value < min_val) or (max_val is not None and value > max_val):
                print(f"Please enter a number between {min_val} and {max_val}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main application loop.
def main():
    manager = PlayerManager()
    
    while True:
        display_menu()
        choice = get_int_input("Enter your choice (1-7): ", 1, 7)
        
        # Add New Player
        if choice == 1: 
            print("\nAdd New Player")
            print("-".center(50,"-"))
            name = input("Enter player name: ").strip()
            number = get_int_input(
                f"Enter jersey number ({MIN_JERSEY_NUMBER}-{MAX_JERSEY_NUMBER}): ",
                MIN_JERSEY_NUMBER, MAX_JERSEY_NUMBER
            )
            manager.add_player(name, number)
        
        # Search by Name
        elif choice == 2:  
            print("\nSearch by Name")
            print("-".center(50,"-"))
            name = input("Enter player name to search: ").strip()
            player = manager.get_player_by_name(name)
            if player:
                print(f"Found: {player}")
            else:
                print(f"No player found with name containing '{name}'.")
        
        # Search by Number
        elif choice == 3:  
            print("\nSearch by Jersey Number")
            print("-".center(50,"-"))
            number = get_int_input(
                f"Enter jersey number ({MIN_JERSEY_NUMBER}-{MAX_JERSEY_NUMBER}): ",
                MIN_JERSEY_NUMBER, MAX_JERSEY_NUMBER
            )
            player = manager.get_player_by_number(number)
            if player:
                print(f"Found: {player}")
            else:
                print(f"No player found with jersey number #{number}.")
        
        # List All Players
        elif choice == 4:  
            manager.list_players()
        
        # Update Player
        elif choice == 5:  
            print("\nUpdate Player Information")
            print("-".center(50,"-"))
            old_number = get_int_input(
                "Enter current jersey number of player to update: ",
                MIN_JERSEY_NUMBER, MAX_JERSEY_NUMBER
            )
            new_name = input("Enter new name (leave blank to keep current): ").strip()
            new_number = get_int_input(
                f"Enter new jersey number ({MIN_JERSEY_NUMBER}-{MAX_JERSEY_NUMBER}, or 0 to keep current): ",
                MIN_JERSEY_NUMBER, MAX_JERSEY_NUMBER
            )
            
            # Get current player info
            current_player = manager.get_player_by_number(old_number)
            if not current_player:
                continue
            
            # Use current values if new ones aren't provided
            final_name = new_name if new_name else current_player.name
            final_number = new_number if new_number != 0 else current_player.jersey_number
            
            manager.update_player(old_number, final_name, final_number)
        
        # Delete Player
        elif choice == 6:  
            print("\nDelete Player")
            print("-".center(50,"-"))
            number = get_int_input(
                "Enter jersey number of player to delete: ",
                MIN_JERSEY_NUMBER, MAX_JERSEY_NUMBER
            )
            manager.delete_player(number)
        
        # Exit
        elif choice == 7:  
            print("\nThank you for using the Player Jersey Number Checker. Goodbye!")
            break
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()