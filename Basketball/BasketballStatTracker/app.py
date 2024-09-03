# Importing necessary libraries
import matplotlib.pyplot as plt

# BasketballPlayer class definition
class BasketballPlayer:
    """Initialize the player with a name and empty statistics."""
    def __init__(self, name):
        self.name = name
        self.games_played = 0
        self.total_points = 0
        self.total_rebounds = 0
        self.total_assists = 0
        self.shots_attempted = 0
        self.shots_made = 0

    # Add statistics for a single game.
    def add_game_stats(self, points, rebounds, assists, shots_attempted, shots_made):
        self.games_played += 1
        self.total_points += points
        self.total_rebounds += rebounds
        self.total_assists += assists
        self.shots_attempted += shots_attempted
        self.shots_made += shots_made

    # Calculate averages per game.
    def calculate_averages(self):
        if self.games_played == 0:
            return None
        return {
            'points_per_game': self.total_points / self.games_played,
            'rebounds_per_game': self.total_rebounds / self.games_played,
            'assists_per_game': self.total_assists / self.games_played
        }

    # Calculate the shooting percentage.
    def calculate_shooting_percentage(self):
        if self.shots_attempted == 0:
            return 0
        return (self.shots_made / self.shots_attempted) * 100

    # Display the player's statistics.
    def display_stats(self):
        averages = self.calculate_averages()
        shooting_percentage = self.calculate_shooting_percentage()

        print(f"Statistics for {self.name}:")
        print(f"Games Played: {self.games_played}")
        if averages:
            print(f"Points Per Game: {averages['points_per_game']:.2f}")
            print(f"Rebounds Per Game: {averages['rebounds_per_game']:.2f}")
            print(f"Assists Per Game: {averages['assists_per_game']:.2f}")
        else:
            print("No games played yet.")
        print(f"Shooting Percentage: {shooting_percentage:.2f}%\n")

    def plot_stats(self):
        """Plot the player's statistics using Matplotlib."""
        averages = self.calculate_averages()
        shooting_percentage = self.calculate_shooting_percentage()

        if averages:
            categories = ['Points Per Game', 'Rebounds Per Game', 'Assists Per Game', 'Shooting Percentage']
            values = [
                averages['points_per_game'],
                averages['rebounds_per_game'],
                averages['assists_per_game'],
                shooting_percentage
            ]

            plt.figure(figsize=(10, 6))
            plt.bar(categories, values, color=['blue', 'green', 'orange', 'red'])
            plt.title(f'{self.name} - Player Statistics')
            plt.xlabel('Categories')
            plt.ylabel('Values')
            plt.ylim(0, max(values) + 5)
            plt.show()
        else:
            print("No data to plot yet.")

# Function to display the menu
def display_menu():
    """Display the menu for the Basketball Player Statistics System."""
    print("\nBasketball Player Statistics System")
    print("1. Create a new player")
    print("2. Select a player")
    print("3. Add game stats")
    print("4. Display player stats")
    print("5. Plot player stats")
    print("6. Exit")
    print("=".center(50, "="))
    return input("Select an option: ")

# Main code
if __name__ == "__main__":
    # Dictionary to store players
    players = {}
    current_player = None

    while True:
        option = display_menu()

        if option == "1":
            # Create a new player
            player_name = input("Enter the player's name: ")
            if player_name in players:
                print("Player already exists.")
            else:
                players[player_name] = BasketballPlayer(player_name)
                current_player = players[player_name]
                print(f"Player {player_name} created and selected.")

        elif option == "2":
            # Select an existing player
            player_name = input("Enter the player's name: ")
            if player_name in players:
                current_player = players[player_name]
                print(f"Player {player_name} selected.")
            else:
                print("Player not found.")

        elif option == "3":
            # Add game stats to the selected player
            if current_player:
                try:
                    points = int(input("Enter points scored: "))
                    rebounds = int(input("Enter rebounds: "))
                    assists = int(input("Enter assists: "))
                    shots_attempted = int(input("Enter shots attempted: "))
                    shots_made = int(input("Enter shots made: "))
                    current_player.add_game_stats(points, rebounds, assists, shots_attempted, shots_made)
                    print("Game stats added successfully.")
                except ValueError:
                    print("Please enter valid numbers for statistics.")
            else:
                print("No player selected. Please select a player first.")

        elif option == "4":
            # Display stats for the selected player
            if current_player:
                current_player.display_stats()
            else:
                print("No player selected. Please select a player first.")

        elif option == "5":
            # Plot stats for the selected player
            if current_player:
                current_player.plot_stats()
            else:
                print("No player selected. Please select a player first.")

        elif option == "6":
            # Exit
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")
