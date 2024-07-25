# Importing necessary libraries
from abc import ABC, abstractmethod

# Base Class for Person (Viewer and Director)
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


# Inheritance for Viewer
class Viewer(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        self._genres = []

    # Implement the abstract method to get the description of the viewer.
    def get_description(self):
        return f"Viewer: {self.get_name()} (ID: {self.get_id_number()})"

    # Method to subscribe to a genre.
    def subscribe_genre(self, genre):
        self._genres.append(genre)

    # Method to get the list of genres the viewer is subscribed to.
    def get_genres(self):
        return self._genres


# Inheritance for Director
class Director(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        self._movies = []

    # Implement the abstract method to get the description of the director.
    def get_description(self):
        return f"Director: {self.get_name()} (ID: {self.get_id_number()})"

    # Method to add a movie to the director's filmography.
    def add_movie(self, movie):
        self._movies.append(movie)

    # Method to get the list of movies the director has made.
    def get_movies(self):
        return self._movies


# Class for Movie
class Movie:
    def __init__(self, title, genre, director, rating, duration):
        self._title = title
        self._genre = genre
        self._director = director
        self._rating = rating
        self._duration = duration

    # Method to get the description of the movie.
    def get_description(self):
        return f"Movie: {self._title} (Genre: {self._genre}, Rating: {self._rating}/10, Duration: {self._duration} mins), Director: {self._director.get_name()}"

    # Method to get the movie's genre.
    def get_genre(self):
        return self._genre


# Function to print movie details
def print_movie_details(movie):
    print(movie.get_description())


# Function to display the menu
def display_menu():
    print("\nMovie Subscription System")
    print("1. Subscribe to a genre")
    print("2. Display viewer details")
    print("3. Display movie details")
    print("4. Exit")
    print("=".center(50,"="))
    return input("Select an option: ")


# Main code
if __name__ == "__main__":
    # Create instances of directors
    director1 = Director("Steven Spielberg", "D001")
    director2 = Director("Christopher Nolan", "D002")

    # Create instances of movies
    movie1 = Movie("Jurassic Park", "Adventure", director1, 8.1, 127)
    movie2 = Movie("Inception", "Sci-Fi", director2, 8.8, 148)

    # Assign movies to directors
    director1.add_movie(movie1)
    director2.add_movie(movie2)

    # Dictionary to hold viewers
    viewers = {}

    while True:
        option = display_menu()

        if option == "1":
            # Subscribe a viewer to a genre
            viewer_name = input("Enter viewer name: ")
            viewer_id = input("Enter viewer ID: ")
            genre = input("Enter genre to subscribe (Adventure/Sci-Fi): ")

            if viewer_id not in viewers:
                viewers[viewer_id] = Viewer(viewer_name, viewer_id)

            viewer = viewers[viewer_id]
            viewer.subscribe_genre(genre)
            print("Genre subscription successful.")

        elif option == "2":
            # Display viewer details
            viewer_id = input("Enter viewer ID: ")
            if viewer_id in viewers:
                viewer = viewers[viewer_id]
                print(viewer.get_description())
                for genre in viewer.get_genres():
                    print(f" - Subscribed to: {genre}")
            else:
                print("Viewer not found.")

        elif option == "3":
            # Display movie details
            movie_title = input("Enter movie title (Jurassic Park/Inception): ")

            if movie_title == "Jurassic Park":
                print_movie_details(movie1)
            elif movie_title == "Inception":
                print_movie_details(movie2)
            else:
                print("Invalid movie title.")

        elif option == "4":
            # Exit
            break

        else:
            print("Invalid option. Please try again.")
