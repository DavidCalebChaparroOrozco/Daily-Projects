# Importing necessary libraries
import calendar
from datetime import datetime

# Function to check if a year is a leap year
def is_leap_year(year):
    """
    Check if a given year is a leap year.
    A year is a leap year if it is divisible by 4 but not by 100,
    unless it is also divisible by 400.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Function to generate a monthly calendar
def generate_month_calendar(year, month):
    """
    Generate a calendar for a specific month and year.
    Uses the `calendar` module to format the month.
    """
    cal = calendar.month(year, month)
    print(f"Calendar for {calendar.month_name[month]} {year}:\n")
    print(cal)

# Function to generate a yearly calendar
def generate_year_calendar(year):
    """
    Generate a calendar for a specific year.
    Uses the `calendar` module to format the entire year.
    """
    cal = calendar.calendar(year)
    print(f"Calendar for the year {year}:\n")
    print(cal)

# Recursive function to display the calendar
def display_calendar(year=None, month=None):
    """
    Recursively display the calendar for a given month or year.
    If no arguments are provided, it will prompt the user for input.
    """
    if year is None:
        year = int(input("Enter the year (e.g., 2025): "))
    if month is None:
        choice = input("Do you want to display a specific month? (yes/no): ").strip().lower()
        if choice == 'yes':
            month = int(input("Enter the month (1-12): "))
            if month < 1 or month > 12:
                print("Invalid month. Please enter a value between 1 and 12.")
                # Recursively ask again
                return display_calendar(year)  
            generate_month_calendar(year, month)
        else:
            generate_year_calendar(year)
    else:
        generate_month_calendar(year, month)

    # Ask if the user wants to generate another calendar
    another = input("Do you want to generate another calendar? (yes/no): ").strip().lower()
    if another == 'yes':
        display_calendar()  # Recursively call the function again
    else:
        print("Thank you for using the calendar generator!")

# Main function to start the program
def main():
    """
    Main function to start the calendar generator.
    """
    print("Welcome to the Recursive Calendar Generator!")
    display_calendar()

# Entry point of the program
if __name__ == "__main__":
    main()