# Importing necessary libraries
from abc import ABC, abstractmethod

# Base Class for Person (Player and Developer)
class Person(ABC):
    def __init__(self, name, id_number):
        # Encapsulation: Making attributes private
        self._name = name
        self._id_number = id_number

    @abstractmethod
    def get_description(self):
        """
        Abstract method to get the description of the person.
        Subclasses must implement this method.
        """
        pass

    # Getter method to retrieve the name of the person.
    def get_name(self):
        return self._name

    # Getter method to retrieve the ID number of the person.
    def get_id_number(self):
        return self._id_number


# Inheritance for Player
class Player(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        self._games_played = {}
        self._genres = []

    # Implement the abstract method to get the description of the player.
    def get_description(self):
        return f"Player: {self.get_name()} (ID: {self.get_id_number()})"

    # Method to subscribe to a genre.
    def subscribe_genre(self, genre):
        self._genres.append(genre)

    # Method to get the list of genres the player is subscribed to.
    def get_genres(self):
        return self._genres

    # Method to record a game played by the player with a score.
    def record_game(self, game, score):
        self._games_played[game] = score

    # Method to get the player's game history with scores.
    def get_game_history(self):
        return self._games_played


# Inheritance for Developer
class Developer(Person):
    def __init__(self, name, id_number, company):
        super().__init__(name, id_number)
        self._company = company
        self._games_developed = []

    # Implement the abstract method to get the description of the developer.
    def get_description(self):
        return f"Developer: {self.get_name()} (ID: {self.get_id_number()}) from {self._company}"

    # Method to add a game to the developer's portfolio.
    def add_game(self, game):
        self._games_developed.append(game)

    # Method to get the list of games the developer has created.
    def get_games(self):
        return self._games_developed


# Class for Game
class Game:
    def __init__(self, title, genre, developer, rating, release_year):
        self._title = title
        self._genre = genre
        self._developer = developer
        self._rating = rating
        self._release_year = release_year

    # Method to get the description of the game.
    def get_description(self):
        return f"Game: {self._title} (Genre: {self._genre}, Rating: {self._rating}/10, Released: {self._release_year}), Developed by: {self._developer.get_name()}"

    # Method to get the game's genre.
    def get_genre(self):
        return self._genre

    # Method to get the game's release year.
    def get_release_year(self):
        return self._release_year


# Function to print game details
def print_game_details(game):
    print(game.get_description())


# Function to display the menu
def display_menu():
    print("\nVideo Game Subscription System")
    print("1. Register new player")
    print("2. Register new developer")
    print("3. Register new game")
    print("4. Subscribe player to a genre")
    print("5. Display player details")
    print("6. Display game details")
    print("7. Display developer details")
    print("8. Exit")
    print("=".center(50, "="))
    return input("Select an option: ")


# Main code
if __name__ == "__main__":
    # Dictionary to hold players
    players = {}

    # Dictionary to hold developers
    developers = {}

    # Dictionary to hold games
    games = {}

    while True:
        option = display_menu()

        if option == "1":
            # Register new player
            player_name = input("Enter player name: ")
            player_id = input("Enter player ID: ")
            if player_id not in players:
                players[player_id] = Player(player_name, player_id)
                print("Player registered successfully.")
            else:
                print("Player ID already exists.")

        elif option == "2":
            # Register new developer
            developer_name = input("Enter developer name: ")
            developer_id = input("Enter developer ID: ")
            company_name = input("Enter company name: ")
            if developer_id not in developers:
                developers[developer_id] = Developer(developer_name, developer_id, company_name)
                print("Developer registered successfully.")
            else:
                print("Developer ID already exists.")

        elif option == "3":
            # Register new game
            game_title = input("Enter game title: ")
            game_genre = input("Enter game genre: ")
            developer_id = input("Enter developer ID: ")
            if developer_id in developers:
                game_rating = float(input("Enter game rating (0-10): "))
                release_year = int(input("Enter game release year: "))
                developer = developers[developer_id]
                game = Game(game_title, game_genre, developer, game_rating, release_year)
                games[game_title] = game
                developer.add_game(game)
                print("Game registered successfully.")
            else:
                print("Developer ID not found.")

        elif option == "4":
            # Subscribe a player to a genre
            player_id = input("Enter player ID: ")
            if player_id in players:
                genre = input("Enter genre to subscribe (Action/Adventure/RPG/etc.): ")
                player = players[player_id]
                player.subscribe_genre(genre)
                print("Genre subscription successful.")
            else:
                print("Player ID not found.")

        elif option == "5":
            # Display player details
            player_id = input("Enter player ID: ")
            if player_id in players:
                player = players[player_id]
                print(player.get_description())
                for genre in player.get_genres():
                    print(f" - Subscribed to: {genre}")
                game_history = player.get_game_history()
                if game_history:
                    print("Game History:")
                    for game, score in game_history.items():
                        print(f" - {game}: {score}/10")
            else:
                print("Player not found.")

        elif option == "6":
            # Display game details
            game_title = input("Enter game title: ")
            if game_title in games:
                game = games[game_title]
                print_game_details(game)
            else:
                print("Game not found.")

        elif option == "7":
            # Display developer details
            developer_id = input("Enter developer ID: ")
            if developer_id in developers:
                developer = developers[developer_id]
                print(developer.get_description())
                for game in developer.get_games():
                    print(f" - {game.get_description()}")
            else:
                print("Developer not found.")

        elif option == "8":
            # Exit
            break

        else:
            print("Invalid option. Please try again.")
