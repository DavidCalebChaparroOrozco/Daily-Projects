# Represents a player in the bowling league.
class Player:
    def __init__(self, name):
        self.name = name
        self.scores = []  # List to store scores for each match

    # Add a score for the player.
    def add_score(self, score):
        self.scores.append(score)

    # Calculate the average score of the player.
    def average_score(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0


# Represents a team in the bowling league.
class Team:
    def __init__(self, name):
        self.name = name
        self.players = []  # List to store players in the team

    # Add a player to the team.
    def add_player(self, player):
        self.players.append(player)

    # Calculate the average score of the team.
    def team_average(self):
        return sum(player.average_score() for player in self.players) / len(self.players) if self.players else 0


# Represents the bowling league.
class League:
    def __init__(self):
        self.teams = []  # List to store teams in the league

    # Add a team to the league.
    def add_team(self, team):
        self.teams.append(team)

    # Get the rankings of teams based on their average scores.
    def get_rankings(self):
        return sorted(self.teams, key=lambda team: team.team_average(), reverse=True)