# A class to represent a basketball player.
class Player:
    # Initialize a new player with a name and position.
    def __init__(self, name, position):
        """        
        name: str - The name of the player
        position: str - The position of the player (e.g., Guard, Forward, Center)
        """
        self.name = name
        self.position = position
        # Initialize points scored to zero
        self.points = 0  

    # Update the player's points scored.
    def score_points(self, points):
        """        
        points: int - The number of points to add to the player's score
        """
        self.points += points

    # Get the player's statistics as a string.
    def get_stats(self):
        """        
        return: str - The player's name, position, and total points scored
        """
        return f"{self.name} ({self.position}): {self.points} points"


# A class to represent a basketball team.
class Team:
    # Initialize a new team with a name and an empty roster.
    def __init__(self, team_name):
        """        
        team_name: str - The name of the team
        """
        self.team_name = team_name
        self.roster = []  # List to hold players in the team

    # Add a player to the team's roster.
    def add_player(self, player):
        """        
        player: Player - The player object to add to the roster
        """
        self.roster.append(player)

    # Display the team's roster and their statistics.
    def display_roster(self):
        print(f"Roster for {self.team_name}:")
        for player in self.roster:
            print(player.get_stats())

    # Calculate the average points scored by all players in the team.
    def calculate_average_points(self):
        """
        return: float - The average points scored by players
        """
        if not self.roster:
            # Avoid division by zero if there are no players
            return 0  
        
        total_points = sum(player.points for player in self.roster)
        average_points = total_points / len(self.roster)
        
        return average_points


def main():
    # Create a new basketball team
    my_team = Team("Dream Team")

    # Add players to the team
    players = [
        Player("Michael Jordan", "Shooting Guard"),
        Player("LeBron James", "Small Forward"),
        Player("Magic Johnson", "Point Guard"),
        Player("Larry Bird", "Small Forward"),
        Player("Kareem Abdul-Jabbar", "Center"),
        Player("Shaquille O'Neal", "Center"),
        Player("Tim Duncan", "Power Forward"),
        Player("Kobe Bryant", "Shooting Guard"),
        Player("Kevin Durant", "Small Forward"),
        Player("Stephen Curry", "Point Guard")
    ]

    for player in players:
        my_team.add_player(player)

    # Simulate scoring points
    players[0].score_points(30)  # Michael Jordan scores 30 points
    players[1].score_points(25)  # LeBron James scores 25 points
    players[2].score_points(22)  # Magic Johnson scores 22 points
    players[3].score_points(20)  # Larry Bird scores 20 points
    players[4].score_points(28)  # Kareem Abdul-Jabbar scores 28 points
    players[5].score_points(24)  # Shaquille O'Neal scores 24 points
    players[6].score_points(18)  # Tim Duncan scores 18 points
    players[7].score_points(27)  # Kobe Bryant scores 27 points
    players[8].score_points(21)  # Kevin Durant scores 21 points
    players[9].score_points(33)  # Stephen Curry scores 33 points

    # Display the team's roster and their statistics
    my_team.display_roster()

    # Calculate and display average points scored by the team
    avg_points = my_team.calculate_average_points()
    print(f"Average Points Scored by {my_team.team_name}: {avg_points:.2f}")

if __name__ == "__main__":
    main()