# Importing necessary libraries
from faker import Faker
from faker.providers import internet
import csv

# Function to generate user data with the specified number of users.
def generate_user(num_user):
    # Create Faker instance
    fake = Faker()
    # Add the Internet proveder to generate email address and IP address.
    fake.add_provider(internet)
    # Store the user data.
    user_data = []
    # Create a dictionary representing a user with various attributes.
    for _ in range(num_user):
        user = {
            "Name": fake.name(),
            "Email": fake.free_email(),
            "Phone": fake.phone_number(),
            "Birthday": fake.date_of_birth(),
            "Address": fake.address(),
            "City": fake.city(),
            "Country": fake.country(),
            "Job Title": fake.job(),
            "Company": fake.company(),
            "IP Address": fake.ipv4_private(),
            "Credit Card Number": fake.credit_card_number(),
            "Username": fake.user_name(),
            "Website": fake.url()
        }
        user_data.append(user)
    return user_data

# Function to save user data to CSV.
def save_csv(data, filename):
    # Get the keys (column names) from the first dictionary in the data list.
    keys = data[0].keys()
    # Open the CSV file for writing.
    with open(filename, 'w', newline='') as output_file:
        # Create a CSV writer with the specified column names.
        writer = csv.DictWriter(output_file, fieldnames=keys)
        # Write the header row to the CSV file.
        writer.writeheader()
        for user in data:
            writer.writerow(user)
    print(f'[+] Data saved to {filename} successfully.')

# Function to save user data to txt.
def save_txt(data,filename):
    # Open the text file for writing.
    with open(filename, 'w') as output_file:
        # Iterate through each user dictionary.
        for user in data:
            for key, value in user.items():
                output_file.write(f"{key}: {value}\n")
            # Add a newline between users in the text file.
            output_file.write('\n')
    print(f'[+] Data saved to {filename} successfully.')

# Function to print user data vertically.
def print_data_vertically(data):
    for user in data:
        for key, value in user.items():
            print(f"{key}: {value}")
        print()

# Get the number of users from user input.
number_of_users = int(input("Enter the number of users to generate: "))
# Generate user data using the specified number of users.
user_data = generate_user(number_of_users)
# Ask the user if they want to save the data to a file.
save_option = input("Do you want to save the data to a file? (yes/no): ").lower()
# If the user chooses to save the data.
if save_option == 'yes':
    file_type = input("Enter file type (csv/txt/both): ").lower()
    if file_type == 'csv' or file_type == 'both':
        custom_filename_csv = input("Enter the CSV filename (without extension): ")
        # Concatenate the filename with the .csv extension.
        filename_csv = f"{custom_filename_csv}.csv"
        save_csv(user_data, filename_csv)
    if file_type == 'txt' or file_type == 'both':
        custom_filename_txt = input("Enter the TXT filename (without extension): ")
        # Concatenate the filename with the .txt extension.
        filename_txt = f"{custom_filename_txt}.txt"
        save_txt(user_data, filename_txt)
    # If the user entered an invalid file type.
    if file_type not in ['csv', 'txt', 'both']:
        print("Invalid file type. Data not saved.")
    else:
    # Call the print_data_vertically function to print the data vertically.
        print_data_vertically(user_data)