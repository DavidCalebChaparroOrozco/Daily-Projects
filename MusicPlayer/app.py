# Importing necessary libraries
import pywhatkit as py

# Function to display the main menu options
def main_menu():
    print("Main Menu:")
    print("1. Play video on YouTube")
    print("2. Search the web")
    print("3. Get info about")
    print("4. Exit")

# Function to play a video on YouTube
def play_on_youtube():
    query = input("Enter the video you want to play: ")
    py.playonyt(query)

# Function to search the web
def search_web():
    query = input("Enter your search query: ")
    py.search(query)

# Function to get information about a topic
def get_info():
    query = input("Enter what you want info about: ")
    py.info(query)

# Main function to control the flow of the program
def main():
    while True:
        main_menu()
        option = input("Enter selection number (1-4): ")
        
        if option == '1':
            play_on_youtube()
        elif option == '2':
            search_web()
        elif option == '3':
            get_info()
        elif option == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()