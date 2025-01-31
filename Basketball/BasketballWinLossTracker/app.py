# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Scrape NBA standings from Wikipedia
url = "https://en.wikipedia.org/wiki/2024%E2%80%9325_NBA_season"

# 2024-25
# https://en.wikipedia.org/wiki/2024%E2%80%9325_NBA_season

# 2023–24
# https://en.wikipedia.org/wiki/2023%E2%80%9324_NBA_season

# 2022-23
# https://en.wikipedia.org/wiki/2022%E2%80%9323_NBA_season


tables = pd.read_html(url)

# Find all division tables (they have columns "W" and "L")
division_tables = [table for table in tables if "W" in table.columns and "L" in table.columns]

# Clean each division table
cleaned_tables = []
for table in division_tables:
    # Rename the first column to "Team"
    table = table.rename(columns={table.columns[0]: "Team"})
    
    # Remove rows where "Team" is NaN or empty
    table = table.dropna(subset=["Team"])
    
    # Keep only relevant columns (Team, W, L, PCT, GB, Home, Road, Div, GP)
    relevant_columns = ["Team", "W", "L", "PCT", "GB", "Home", "Road", "Div", "GP"]
    table = table[[col for col in relevant_columns if col in table.columns]]
    
    # Append the cleaned table to the list
    cleaned_tables.append(table)

# Combine all cleaned division tables into one DataFrame
standings = pd.concat(cleaned_tables, ignore_index=True)

# Clean the team names (remove prefixes like "x –" or "y –")
standings["Team"] = standings["Team"].str.replace(r"[x-y] – ", "", regex=True)

# Display the combined standings table
print(standings.head())

# List all teams with their corresponding numbers
print("\nList of Teams:")
for idx, team in enumerate(standings["Team"], start=1):
    print(f"{idx}. {team}")

# Allow the user to select a team by number
team_number = int(input("\nEnter the number of the team you want to visualize: ")) - 1

# Validate the team number
if 0 <= team_number < len(standings):
    selected_team = standings.iloc[team_number]
    team_name = selected_team["Team"]
    wins = selected_team["W"]
    losses = selected_team["L"]
    pct = selected_team["PCT"]  # Winning percentage
    game_behind = selected_team.get("GB", "N/A")  # Games behind
    home_record = selected_team.get("Home", "N/A")  # Home record
    road_record = selected_team.get("Road", "N/A")  # Road record
    div_record = selected_team.get("Div", "N/A")  # Division record
    games_played = selected_team.get("GP", "N/A")  # Games played

    # Display team statistics
    print(f"\n{team_name} 2024-25 Season Record:")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Winning Percentage (PCT): {pct}")
    print(f"Games Behind (GB): {game_behind}")
    print(f"Home Record (Home): {home_record}")
    print(f"Road Record (Road): {road_record}")
    print(f"Division Record (Div): {div_record}")
    print(f"Games Played (GP): {games_played}")

    # Plot the data
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(f"{team_name} 2024-25 Season Statistics", fontsize=16)

    # Bar plot for wins and losses of the selected team
    axes[0, 0].bar(["Wins", "Losses"], [wins, losses], color=["green", "red"])
    axes[0, 0].set_title("Wins vs Losses")
    axes[0, 0].set_ylabel("Number of Games")

    # Stacked bar plot for wins and losses of all teams
    teams = standings["Team"]
    wins_all = standings["W"]
    losses_all = standings["L"]

    axes[0, 1].bar(teams, wins_all, color="green", label="Wins")
    axes[0, 1].bar(teams, losses_all, bottom=wins_all, color="red", label="Losses")
    axes[0, 1].set_title("Wins and Losses by Team")
    axes[0, 1].set_ylabel("Number of Games")
    # Rotate team names for better readability
    axes[0, 1].tick_params(axis="x", rotation=90)  

    # Highlight the selected team in the stacked bar plot
    selected_index = team_number
    axes[0, 1].bar(selected_index, wins_all[selected_index], color="blue", label=f"Selected: {team_name}")
    axes[0, 1].bar(selected_index, losses_all[selected_index], bottom=wins_all[selected_index], color="blue")
    axes[0, 1].legend()

    # Histogram of winning percentages
    sns.histplot(standings["PCT"], bins=10, kde=True, ax=axes[1, 0])
    axes[1, 0].set_title("Distribution of Winning Percentages")
    axes[1, 0].set_xlabel("Winning Percentage (PCT)")
    axes[1, 0].set_ylabel("Frequency")

    # Box plot for wins
    sns.boxplot(x=standings["W"], ax=axes[1, 1])
    axes[1, 1].set_title("Distribution of Wins")
    axes[1, 1].set_xlabel("Wins")

    plt.tight_layout()
    plt.show()
else:
    print("Invalid team number. Please try again.")