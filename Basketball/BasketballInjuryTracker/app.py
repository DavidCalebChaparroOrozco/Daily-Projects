# Class to represent a basketball player.
class Player:
    def __init__(self, name):
        self.name = name
        # List to store injury records
        self.injuries = []  

    # Add an injury record for the player.
    def add_injury(self, injury):
        self.injuries.append(injury)

    # Return the player's injury history.
    def get_injury_history(self):
        return self.injuries

# Class to represent an injury record.
class Injury:
    def __init__(self, type_of_injury, recovery_time):
        self.type_of_injury = type_of_injury
        # Recovery time in days
        self.recovery_time = recovery_time  

# Class to represent the medical team.
class MedicalTeam:
    # Notify the medical team about a new injury.
    def notify(self, player_name, injury):
        print(f"Notification: {player_name} has sustained a {injury.type_of_injury}. Estimated recovery time: {injury.recovery_time} days.")

# Main class to track injuries of players.
class InjuryTracker:
    def __init__(self):
        # Dictionary to store players by name
        self.players = {}  
        self.medical_team = MedicalTeam()

    # Add a new player to the tracker.
    def add_player(self, name):
        if name not in self.players:
            self.players[name] = Player(name)
            print(f"Player {name} added.")
        else:
            print(f"Player {name} already exists.")

    # Record an injury for a player and notify the medical team.
    def record_injury(self, player_name, type_of_injury, recovery_time):
        if player_name in self.players:
            injury = Injury(type_of_injury, recovery_time)
            self.players[player_name].add_injury(injury)
            self.medical_team.notify(player_name, injury)
        else:
            print(f"Player {player_name} not found.")

    # Retrieve the injury history of a player.
    def get_player_history(self, player_name):
        if player_name in self.players:
            return self.players[player_name].get_injury_history()
        else:
            print(f"Player {player_name} not found.")
            return None

# Display the main menu options for the Basketball Injury Tracker.
def display_menu():
    print("\nBasketball Injury Tracker")
    print("1. Add new player")
    print("2. Record injury for a player")
    print("3. View injury history for a player")
    print("4. Exit")
    print("=".center(50, "="))
    return input("Select an option: ")

def main():
    tracker = InjuryTracker()

    while True:
        option = display_menu()

        if option == '1':
            player_name = input("Enter the name of the player: ")
            tracker.add_player(player_name)

        elif option == '2':
            player_name = input("Enter the name of the player: ")
            type_of_injury = input("Enter the type of injury: ")
            recovery_time = int(input("Enter recovery time in days: "))
            tracker.record_injury(player_name, type_of_injury, recovery_time)

        elif option == '3':
            player_name = input("Enter the name of the player: ")
            injuries = tracker.get_player_history(player_name)
            if injuries:
                print("\nInjury History:")
                for injury in injuries:
                    print(f"- {injury.type_of_injury}, Recovery Time: {injury.recovery_time} days")
            else:
                print(f"No injury history found for {player_name}.")

        elif option == '4':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()