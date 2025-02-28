# Handles user input and output.
class View:
    @staticmethod
    # Display the main menu.
    def display_menu():
        print("Bowling League Rankings:")
        print("1. Register Player")
        print("2. Register Team")
        print("3. Enter Match Results")
        print("4. Show League Rankings")
        print("5. Exit")

    @staticmethod
    # Get input from the user.
    def get_input(prompt):
        return input(prompt)

    @staticmethod
    # Display a message to the user.
    def show_message(message):
        print(message)

    @staticmethod
    # Display the league rankings.
    def show_rankings(teams):
        print("League Rankings:".center(30, "-"))
        for i, team in enumerate(teams, start=1):
            print(f"{i}. {team.name} - Average Score: {team.team_average():.2f}")