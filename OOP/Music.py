# Importing necessary libraries
from abc import ABC, abstractmethod

# Base Class for Person (Listener and Artist)
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


# Inheritance for Listener
class Listener(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        self._genres = []

    # Implement the abstract method to get the description of the listener.
    def get_description(self):
        return f"Listener: {self.get_name()} (ID: {self.get_id_number()})"

    # Method to subscribe to a genre.
    def subscribe_genre(self, genre):
        self._genres.append(genre)

    # Method to get the list of genres the listener is subscribed to.
    def get_genres(self):
        return self._genres


# Inheritance for Artist
class Artist(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        self._songs = []

    # Implement the abstract method to get the description of the artist.
    def get_description(self):
        return f"Artist: {self.get_name()} (ID: {self.get_id_number()})"

    # Method to add a song to the artist's discography.
    def add_song(self, song):
        self._songs.append(song)

    # Method to get the list of songs the artist has made.
    def get_songs(self):
        return self._songs


# Class for Song
class Song:
    def __init__(self, title, genre, artist, rating, duration):
        self._title = title
        self._genre = genre
        self._artist = artist
        self._rating = rating
        self._duration = duration

    # Method to get the description of the song.
    def get_description(self):
        return f"Song: {self._title} (Genre: {self._genre}, Rating: {self._rating}/10, Duration: {self._duration} mins), Artist: {self._artist.get_name()}"

    # Method to get the song's genre.
    def get_genre(self):
        return self._genre


# Function to print song details
def print_song_details(song):
    print(song.get_description())


# Function to display the menu
def display_menu():
    print("\nMusic Subscription System")
    print("1. Register new listener")
    print("2. Register new artist")
    print("3. Register new song")
    print("4. Subscribe listener to a genre")
    print("5. Display listener details")
    print("6. Display song details")
    print("7. Display artist details")
    print("8. Exit")
    print("=".center(50, "="))
    return input("Select an option: ")


# Main code
if __name__ == "__main__":
    # Dictionary to hold listeners
    listeners = {}

    # Dictionary to hold artists
    artists = {}

    # Dictionary to hold songs
    songs = {}

    while True:
        option = display_menu()

        if option == "1":
            # Register new listener
            listener_name = input("Enter listener name: ")
            listener_id = input("Enter listener ID: ")
            if listener_id not in listeners:
                listeners[listener_id] = Listener(listener_name, listener_id)
                print("Listener registered successfully.")
            else:
                print("Listener ID already exists.")

        elif option == "2":
            # Register new artist
            artist_name = input("Enter artist name: ")
            artist_id = input("Enter artist ID: ")
            if artist_id not in artists:
                artists[artist_id] = Artist(artist_name, artist_id)
                print("Artist registered successfully.")
            else:
                print("Artist ID already exists.")

        elif option == "3":
            # Register new song
            song_title = input("Enter song title: ")
            song_genre = input("Enter song genre: ")
            artist_id = input("Enter artist ID: ")
            if artist_id in artists:
                song_rating = float(input("Enter song rating (0-10): "))
                song_duration = int(input("Enter song duration (in minutes): "))
                artist = artists[artist_id]
                song = Song(song_title, song_genre, artist, song_rating, song_duration)
                songs[song_title] = song
                artist.add_song(song)
                print("Song registered successfully.")
            else:
                print("Artist ID not found.")

        elif option == "4":
            # Subscribe a listener to a genre
            listener_id = input("Enter listener ID: ")
            if listener_id in listeners:
                genre = input("Enter genre to subscribe (Pop/Rock/Jazz/etc.): ")
                listener = listeners[listener_id]
                listener.subscribe_genre(genre)
                print("Genre subscription successful.")
            else:
                print("Listener ID not found.")

        elif option == "5":
            # Display listener details
            listener_id = input("Enter listener ID: ")
            if listener_id in listeners:
                listener = listeners[listener_id]
                print(listener.get_description())
                for genre in listener.get_genres():
                    print(f" - Subscribed to: {genre}")
            else:
                print("Listener not found.")

        elif option == "6":
            # Display song details
            song_title = input("Enter song title: ")
            if song_title in songs:
                song = songs[song_title]
                print_song_details(song)
            else:
                print("Song not found.")

        elif option == "7":
            # Display artist details
            artist_id = input("Enter artist ID: ")
            if artist_id in artists:
                artist = artists[artist_id]
                print(artist.get_description())
                for song in artist.get_songs():
                    print(f" - {song.get_description()}")
            else:
                print("Artist not found.")

        elif option == "8":
            # Exit
            break

        else:
            print("Invalid option. Please try again.")