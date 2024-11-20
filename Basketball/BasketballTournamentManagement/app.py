# Import necessary libraries
from datetime import datetime, timedelta
import random

class Player:
    def __init__(self, name, position):
        # Player's name
        self.name = name  
        # Player's position
        self.position = position  

class Team:
    def __init__(self, name):
        # Team's name
        self.name = name  
        # List to store players
        self.players = []  
        # Number of wins
        self.wins = 0  
        # Number of losses
        self.losses = 0  

    # Add a player to the team.
    def add_player(self, player):
        self.players.append(player)

    # Record a win for the team.
    def record_win(self):
        self.wins += 1

    # Record a loss for the team.
    def record_loss(self):
        self.losses += 1

    # Return the team's win-loss record.
    def get_record(self):
        return f"{self.wins}-{self.losses}"

class Match:
    def __init__(self, team_a, team_b, date_time):
        # First team
        self.team_a = team_a  
        # Second team
        self.team_b = team_b  
        # Match date and time
        self.date_time = date_time  
        # Match result
        self.result = None  

    # Set the result of the match.
    def set_result(self, result):
        self.result = result
        if result == 'A':
            self.team_a.record_win()
            self.team_b.record_loss()
        elif result == 'B':
            self.team_b.record_win()
            self.team_a.record_loss()

class Tournament:
    def __init__(self):
        # List of teams participating in the tournament
        self.teams = []  
        # List of matches scheduled
        self.matches = []  

    # Register a new team in the tournament.
    def register_team(self, team):
        self.teams.append(team)

    # Create a schedule for matches between all teams.
    def create_schedule(self):
        # Shuffle teams for random pairing
        random.shuffle(self.teams)  
        for i in range(0, len(self.teams), 2):
                # Ensure there is a pair
            if i + 1 < len(self.teams):  
                # Schedule matches on consecutive days
                match_time = datetime.now() + timedelta(days=(i // 2))  
                match = Match(self.teams[i], self.teams[i + 1], match_time)
                self.matches.append(match)

    # Display the standings of all teams.
    def display_standings(self):
        print("Standings:")
        for team in sorted(self.teams, key=lambda t: (t.wins, t.losses), reverse=True):
            print(f"{team.name}: {team.get_record()}")

# Display the main menu for the Basketball Tournament Management System.
def display_menu():
    print("\nBasketball Tournament Management System")
    print("1. Register a team")
    print("2. Register a player")
    print("3. Create match schedule")
    print("4. Record match result")
    print("5. Display standings")
    print("6. Exit")
    print("=".center(50, "="))
    return input("Select an option: ")

def main():
    # Create an instance of the Tournament class
    tournament = Tournament()  

    while True:
        # Display the menu and get user input
        option = display_menu()  

        if option == "1":
            # Register a team
            team_name = input("Enter team name: ")
            team = Team(team_name)
            tournament.register_team(team)
            print(f"Team '{team_name}' registered successfully.")

        elif option == "2":
            # Register a player
            team_name = input("Enter the team name to add a player: ")
            team = next((t for t in tournament.teams if t.name == team_name), None)
            if team:
                player_name = input("Enter player name: ")
                position = input("Enter player position: ")
                player = Player(player_name, position)
                team.add_player(player)
                print(f"Player '{player_name}' added to team '{team_name}'.")
            else:
                print(f"Team '{team_name}' not found.")

        elif option == "3":
            # Create match schedule
            tournament.create_schedule()
            print("Match schedule created successfully.")

        elif option == "4":
            # Record match result
            match_index = int(input("Enter match index (starting from 0): "))
            result = input("Enter result (A for Team A wins, B for Team B wins): ")
            if result in ['A', 'B'] and 0 <= match_index < len(tournament.matches):
                tournament.matches[match_index].set_result(result)
                print(f"Result recorded for match {match_index}.")
            else:
                print("Invalid input. Please try again.")

        elif option == "5":
            # Display standings
            tournament.display_standings()

        elif option == "6":
            # Exit the program
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please select a valid menu option.")

# Entry point of the program
if __name__ == "__main__":
    main()