# Initialize the calendar with surprises for each day
class AdventCalendar:
    def __init__(self):
        self.days = {
            1: "A quote about Christmas: 'Christmas isn't just a day, it's a state of mind.'",
            2: "Mini-game: Guess the Christmas song!",
            3: "Recipe: How to make gingerbread cookies.",
            4: "Fun fact: Did you know that the first artificial Christmas tree was made in Germany?",
            5: "Activity: Write a letter to Santa.",
            6: "Craft idea: Make your own ornaments.",
            7: "Movie suggestion: 'Home Alone'.",
            8: "Christmas trivia quiz.",
            9: "A quote about giving: 'It's not how much we give but how much love we put into giving.'",
            10: "Mini-game: Christmas word search.",
        }

    # Display the content for the given day.
    def display_day(self, day):
        if day in self.days:
            print(f"Day {day}: {self.days[day]}")
        else:
            print("This day has no surprise!")

    # Recursively navigate through the calendar.
    def navigate(self, current_day):
        self.display_day(current_day)
        
        # Ask user if they want to continue or go back
        choice = input("Would you like to go to the next day (n), go back (b), or exit (e)? ").strip().lower()
        
        if choice == 'n':
            if current_day < len(self.days):
                self.navigate(current_day + 1)
            else:
                print("You've reached the end of the calendar!")
                self.exit_calendar()
        elif choice == 'b':
            if current_day > 1:
                self.navigate(current_day - 1)
            else:
                print("You are at the first day. You cannot go back.")
                self.exit_calendar()
        elif choice == 'e':
            self.exit_calendar()
        else:
            print("Invalid choice. Please try again.")
            self.navigate(current_day)

    # Exit the calendar.
    def exit_calendar(self):
        print("Thank you for exploring the Advent Calendar! Merry Christmas!")
        exit()

# Main function to run the Advent Calendar.
def main():
    calendar = AdventCalendar()
    print("Welcome to the Advent Calendar!")
    calendar.navigate(1)

if __name__ == "__main__":
    main()
