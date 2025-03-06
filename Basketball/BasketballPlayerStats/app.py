# Import necessary libraries
import json
import matplotlib.pyplot as plt
from itertools import groupby
from collections import defaultdict, Counter
from functools import reduce
from operator import itemgetter

# Sample data: List of players and their stats (points, rebounds, assists)
players = ["LeBron James", "Stephen Curry", "Kevin Durant", "Giannis Antetokounmpo", "Luka Doncic"]
# Points per game
points = [28, 32, 27, 30, 29]  
# Rebounds per game
rebounds = [8, 5, 7, 12, 9]    
# Assists per game
assists = [9, 8, 6, 6, 10]      

# Function to display player stats with their rank using enumerate()
def display_player_stats(players, points, rebounds, assists):
    print("Player Stats:")
    # Use enumerate to get both index and player name
    for rank, (player, pts, reb, ast) in enumerate(zip(players, points, rebounds, assists), start=1):
        print(f"Rank {rank}: {player} - {pts} pts, {reb} reb, {ast} ast")

# Function to filter players with more than 25 points per game
def filter_high_scorers(players, points):
    print("\nHigh Scorers (Players with more than 25 points per game):")
    # Use filter to get players with more than 25 points
    high_scorers = filter(lambda x: x[1] > 25, zip(players, points))
    for player, pts in high_scorers:
        print(f"{player}: {pts} pts")

# Function to find the player with the most rebounds
def find_top_rebounder(players, rebounds):
    print("\nTop Rebounder:")
    # Use zip to pair players with rebounds and max to find the top rebounder
    top_rebounder = max(zip(players, rebounds), key=lambda x: x[1])
    print(f"{top_rebounder[0]} with {top_rebounder[1]} rebounds per game")

# Function to calculate average stats
def calculate_average_stats(points, rebounds, assists):
    avg_points = sum(points) / len(points)
    avg_rebounds = sum(rebounds) / len(rebounds)
    avg_assists = sum(assists) / len(assists)
    print(f"\nAverage Stats: {avg_points:.2f} pts, {avg_rebounds:.2f} reb, {avg_assists:.2f} ast")

# Function to save data to a JSON file
def save_data_to_json(players, points, rebounds, assists, filename='player_stats.json'):
    data = {
        "players": players,
        "points": points,
        "rebounds": rebounds,
        "assists": assists
    }
    with open(filename, 'w') as f:
        json.dump(data, f)
    print(f"\nData saved to {filename}")

# Function to load data from a JSON file
def load_data_from_json(filename='player_stats.json'):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        print(f"\nData loaded from {filename}")
        return data['players'], data['points'], data['rebounds'], data['assists']
    except FileNotFoundError:
        print(f"\nFile {filename} not found. Using default data.")
        return players, points, rebounds, assists

# Function to plot player stats
def plot_player_stats(players, points, rebounds, assists):
    plt.figure(figsize=(10, 5))
    plt.bar(players, points, label='Points')
    plt.bar(players, rebounds, label='Rebounds', alpha=0.5)
    plt.bar(players, assists, label='Assists', alpha=0.5)
    plt.xlabel('Players')
    plt.ylabel('Stats')
    plt.title('Player Stats Comparison')
    plt.legend()
    plt.show()

# Function to group players by their points range using itertools.groupby
def group_players_by_points_range(players, points):
    print("\nPlayers Grouped by Points Range:")
    # Sort players and points together
    sorted_data = sorted(zip(players, points), key=itemgetter(1))
    # Group by points range (e.g., 25-30, 30-35)
    for key, group in groupby(sorted_data, key=lambda x: (x[1] // 5) * 5):
        print(f"Points Range {key}-{key + 5}:")
        for player, pts in group:
            print(f"  {player}: {pts} pts")

# Function to count players with the same number of rebounds using collections.Counter
def count_rebounds_frequency(rebounds):
    print("\nRebounds Frequency:")
    rebound_counts = Counter(rebounds)
    for rebounds, count in rebound_counts.items():
        print(f"{rebounds} rebounds: {count} player(s)")

# Function to find the total points using functools.reduce
def calculate_total_points(points):
    total_points = reduce(lambda x, y: x + y, points)
    print(f"\nTotal Points by All Players: {total_points}")

# Function to create a dictionary of players and their stats using collections.defaultdict
def create_player_stats_dict(players, points, rebounds, assists):
    player_stats = defaultdict(dict)
    for player, pts, reb, ast in zip(players, points, rebounds, assists):
        player_stats[player] = {"points": pts, "rebounds": reb, "assists": ast}
    print("\nPlayer Stats Dictionary:")
    for player, stats in player_stats.items():
        print(f"{player}: {stats}")

# Main function to run the program
def main():
    # Load data from JSON file or use default data
    players, points, rebounds, assists = load_data_from_json()

    # Display player stats with ranks
    display_player_stats(players, points, rebounds, assists)

    # Filter and display high scorers
    filter_high_scorers(players, points)

    # Find and display the top rebounder
    find_top_rebounder(players, rebounds)

    # Calculate and display average stats
    calculate_average_stats(points, rebounds, assists)

    # Save data to JSON file
    save_data_to_json(players, points, rebounds, assists)

    # Plot player stats
    plot_player_stats(players, points, rebounds, assists)

    # Group players by points range
    group_players_by_points_range(players, points)

    # Count frequency of rebounds
    count_rebounds_frequency(rebounds)

    # Calculate total points using reduce
    calculate_total_points(points)

    # Create a dictionary of player stats
    create_player_stats_dict(players, points, rebounds, assists)

# Run the program
if __name__ == "__main__":
    main()