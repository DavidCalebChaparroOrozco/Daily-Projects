from model.person import Reader, Author
from model.book import Book
from view.view import View

# Controller class to handle the business logic
class Controller:
    def __init__(self):
        self.viewers = {}
        self.authors = {}
        self.books = []

    def add_author(self, name, id_number):
        if id_number not in self.authors:
            self.authors[id_number] = Author(name, id_number)

    def add_book(self, title, genre, author_id, rating, pages):
        if author_id in self.authors:
            author = self.authors[author_id]
            book = Book(title, genre, author, rating, pages)
            author.add_book(book)
            self.books.append(book)

    def subscribe_reader_to_genre(self, reader_id, reader_name, genre):
        if reader_id not in self.viewers:
            self.viewers[reader_id] = Reader(reader_name, reader_id)

        viewer = self.viewers[reader_id]
        viewer.subscribe_genre(genre)
        View.show_message("Genre subscription successful.")

    def display_reader_details(self, reader_id):
        if reader_id in self.viewers:
            reader = self.viewers[reader_id]
            View.show_message(reader.get_description())
            for genre in reader.get_genres():
                View.show_message(f" - Subscribed to: {genre}")
        else:
            View.show_message("Reader not found.")

    def display_book_details(self, title):
        for book in self.books:
            if book.get_description().startswith(f"Book: {title}"):
                View.show_message(book.get_description())
                return
        View.show_message("Invalid book title.")
