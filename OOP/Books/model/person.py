from abc import ABC, abstractmethod

# Base class for Person (Reader and Author)
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

    # Getter method to retrieve the name of the person
    def get_name(self):
        return self._name

    # Getter method to retrieve the ID number of the person
    def get_id_number(self):
        return self._id_number


# Reader class inheriting from Person
class Reader(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        self._genres = []

    def get_description(self):
        return f"Reader: {self.get_name()} (ID: {self.get_id_number()})"

    def subscribe_genre(self, genre):
        self._genres.append(genre)

    def get_genres(self):
        return self._genres


# Author class inheriting from Person
class Author(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        self._books = []

    def get_description(self):
        return f"Author: {self.get_name()} (ID: {self.get_id_number()})"

    def add_book(self, book):
        self._books.append(book)

    def get_books(self):
        return self._books
