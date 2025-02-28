from model.model import Player, Team, League
from view.view import View

# Manages the flow of the application.
class Controller:
    def __init__(self):
        self.league = League()
        self.view = View()

    # Run the application.
    def run(self):
        while True:
            self.view.display_menu()
            choice = self.view.get_input("Choose an option: ")

            if choice == "1":
                self.register_player()
            elif choice == "2":
                self.register_team()
            elif choice == "3":
                self.enter_match_results()
            elif choice == "4":
                self.show_rankings()
            elif choice == "5":
                self.view.show_message("Exiting the program. Goodbye!")
                break
            else:
                self.view.show_message("Invalid option. Please try again.")

    # Register a new player.
    def register_player(self):
        name = self.view.get_input("Enter player name: ")
        player = Player(name)
        team_name = self.view.get_input("Enter team name to add the player to: ")
        team = self._find_team(team_name)
        if team:
            team.add_player(player)
            self.view.show_message(f"Player {name} added to team {team_name}.")
        else:
            self.view.show_message(f"Team {team_name} not found.")

    # Register a new team.
    def register_team(self):
        name = self.view.get_input("Enter team name: ")
        team = Team(name)
        self.league.add_team(team)
        self.view.show_message(f"Team {name} registered.")

    # Enter match results for a player.
    def enter_match_results(self):
        player_name = self.view.get_input("Enter player name: ")
        score = int(self.view.get_input("Enter player score: "))
        for team in self.league.teams:
            for player in team.players:
                if player.name == player_name:
                    player.add_score(score)
                    self.view.show_message(f"Score {score} added for player {player_name}.")
                    return
        self.view.show_message(f"Player {player_name} not found.")

    # Show the league rankings.
    def show_rankings(self):
        rankings = self.league.get_rankings()
        self.view.show_rankings(rankings)

    # Find a team by name.
    def _find_team(self, name):
        for team in self.league.teams:
            if team.name == name:
                return team
        return None