# Importing necessary libraries
import string
import random
import csv

# Function to get user input
def get_user_input():
    while True:
        try:
            # Ask the user for the number of characters for the password
            user_input = int(input("How many characters do you want in your password? "))
            # Check if the entered number is less than 8
            if user_input < 8:
                print("Your number should be at least 8.")
            else:
                # Return the number of characters if it's valid
                return user_input
        except ValueError:
            # Handle error if the user enters a non-numeric value
            print("Please, enter numbers only.")

# Function to generate the password
def generate_password(characters_number):
    # List of valid characters for the password
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)

    # Calculate the lengths of password parts based on ratio
    part1_length = round(characters_number * 0.6)
    part2_length = round(characters_number * 0.4)

    # Randomly generate password parts
    password_part1 = random.choices(lowercase + uppercase, k=part1_length)
    password_part2 = random.choices(digits + punctuation, k=part2_length)

    # Concatenate password parts and shuffle them
    password = ''.join(password_part1 + password_part2)
    shuffled_password = ''.join(random.sample(password, len(password)))
    # Return the shuffled password
    return shuffled_password

# Function to save the generated password to a CSV file
def save_password(password):
    with open('passwords.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([password])

# Main program function
def main():
    # Get user input for the number of password characters
    characters_number = get_user_input()
    # Generate the password based on the specified number of characters
    password = generate_password(characters_number)
    # Print the generated password
    print("Strong Password:", password)
    # Save the passwords
    save_password(password)

# Program entry point
if __name__ == "__main__":
    main()
