# Class for Book
class Book:
    def __init__(self, title, genre, author, rating, pages):
        self._title = title
        self._genre = genre
        self._author = author
        self._rating = rating
        self._pages = pages

    def get_description(self):
        return f"Book: {self._title} (Genre: {self._genre}, Rating: {self._rating}/10, Pages: {self._pages}), Author: {self._author.get_name()}"

    def get_genre(self):
        return self._genre
