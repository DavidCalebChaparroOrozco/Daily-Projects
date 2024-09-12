# Importing necessary libraries
import random
import matplotlib.pyplot as plt
import numpy as np

# List of possible positions for players
positions = ['Point Guard', 'Shooting Guard', 'Small Forward', 'Power Forward', 'Center']

# Function to generate a random player
def generate_player():
    player = {
        'Name': f'Player_{random.randint(100, 999)}',
        'Height': round(random.uniform(1.75, 2.20), 2),  # Height in meters
        'Position': random.choice(positions),
        # Points per game
        'PTS': round(random.uniform(5, 35), 1),  
        # Rebounds per game
        'REB': round(random.uniform(3, 15), 1),  
        # Assists per game
        'AST': round(random.uniform(2, 12), 1),  
        # Field Goal Percentage
        'FG%': round(random.uniform(40, 60), 1)  
    }
    return player

# Function to display player stats in a polar bar chart
def plot_player_stats(player):
    stats = ['REB', 'AST', 'FG%']
    values = [player['REB'], player['AST'], player['FG%']]
    
    # Convert stats to a bar chart on a polar axis
    N = len(stats)
    theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
    radii = values
    width = np.pi / 4 * 0.8  # Set a fixed width for better visibility
    colors = plt.cm.viridis(np.array(values) / max(values))

    ax = plt.subplot(projection='polar')
    bars = ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=0.7)

    # Set the labels at each bar (angles)
    ax.set_xticks(theta)
    ax.set_xticklabels(stats)

    # Add a title and grid for better readability
    ax.set_title(f"Stats for {player['Name']}", va='bottom')
    ax.grid(True)

    # Add value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.5, f'{height}', ha='center', va='bottom')

    plt.show()

# Function to display points in a separate bar chart
def plot_points(player):
    plt.figure(figsize=(6, 4))
    plt.bar(player['Name'], player['PTS'], color='blue', alpha=0.7)
    plt.title(f"Points for {player['Name']}")
    plt.ylabel("Points per Game (PTS)")
    plt.ylim(0, 40)  # Set y-axis limit for better visibility
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Function to form a team of random players
def create_team(num_players):
    team = [generate_player() for _ in range(num_players)]
    return team

# Function to save team players to a file
def save_team(team, filename="team.txt"):
    with open(filename, 'w') as f:
        for player in team:
            f.write(f"{player['Name']}, Position: {player['Position']}, Height: {player['Height']}m, PTS: {player['PTS']}, REB: {player['REB']}, AST: {player['AST']}, FG%: {player['FG%']}\n")

# Main program
if __name__ == "__main__":
    num_players = int(input("How many players do you want to generate? "))
    
    # Create a team of random players
    team = create_team(num_players)
    
    # Display each player's stats and plot them
    for player in team:
        print(f"Player: {player['Name']}, Position: {player['Position']}, Height: {player['Height']}m")
        print(f"Stats: PTS: {player['PTS']}, REB: {player['REB']}, AST: {player['AST']}, FG%: {player['FG%']}\n")
        # Show bar chart for points
        plot_points(player)  
        # Show polar chart for other stats
        plot_player_stats(player)  
    
    # Option to save the team
    save_option = input("Do you want to save this team to a file? (yes/no) ").lower()
    if save_option == 'yes':
        save_team(team)
        print("Team saved to 'team.txt'.")