# Importing necessary libraries
import sqlite3
from sqlite3 import Error

# Define a class to represent a Book object with attributes: title, author, year_published, and genre.
class Book:
    def __init__(self, title, author, year_published, genre):
        self.title = title  
        self.author = author
        self.year_published = year_published
        self.genre = genre

# Define a class to represent a Bookshelf object with a list to hold books.
class Bookshelf:
    def __init__(self):
        self.books = []

    # Method to add a book to the bookshelf
    def add_book(self, book):
        self.books.append(book)

    # Method to remove a book from the bookshelf
    def remove_book(self, book):
        self.books.remove(book)

    # Method to retrieve all books from the bookshelf
    def get_all_books(self):
        return self.books

# Function to validate and get a valid year input from the user
def input_valid_year():
    while True:
        year = input("Enter the year (YYYY): ")
        if year.isdigit() and len(year) == 4:
            return int(year)
        else:
            print("Invalid input. Please enter a valid year (YYYY).")

# Function to validate and get a valid author input from the user
def input_valid_author():
    while True:
        author = input("Enter the author of the book: ")
        if all(char.isalpha() or char.isspace() for char in author):
            return author.strip()
        else:
            print("Invalid input. Please enter a valid author name.")

# Function to validate and get a valid genre input from the user
def input_valid_genre():
    while True:
        genre = input("Enter the genre of the book: ")
        if all(char.isalpha() or char.isspace() for char in genre):
            return genre.strip()
        else:
            print("Invalid input. Please enter a valid genre.")

# Function to create a connection to a SQLite database
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
    except Error as e:
        print("Error creating connection:", e)
    return conn

# Function to create a table to store bookshelf data in the database
def create_bookshelf_table(conn):
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE Bookshelf 
                (title text, author text, year_published text, genre text)''')
    except Error as e:
        print("Error creating table:", e)

# Function to add a book to the bookshelf table in the database
def add_book_to_shelf(conn, book):
    sql = '''INSERT INTO Bookshelf(title, author, year_published, genre)
            VALUES (?, ?, ?, ?)'''
    c = conn.cursor()
    c.execute(sql, book)
    conn.commit()

# Function to retrieve all books from the bookshelf table in the database
def get_all_books_from_shelf(conn):
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM Bookshelf")
        rows = c.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print("Error fetching books:", e)

# Function to update a book in the bookshelf table in the database
def update_book_in_shelf(conn, old_title, new_book_details):
    sql = '''UPDATE Bookshelf
            SET title = ?,
                author = ?,
                year_published = ?,
                genre = ?
            WHERE title = ?'''
    c = conn.cursor()
    c.execute(sql, (*new_book_details, old_title))
    conn.commit()

# Function to delete a book from the bookshelf table in the database
def delete_book_from_shelf(conn, title):
    sql = '''DELETE FROM Bookshelf WHERE title=?'''
    c = conn.cursor()
    c.execute(sql, (title,))
    conn.commit()

# Function to display the main menu of the Bookshelf Manager.
def display_menu():
    print("Welcome to the Bookshelf Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Update a book")
    print("4. Search books")
    print("5. View all books")
    print("6. Exit")

# Function to add a book using user input
def add_book_menu():
    title = input("Enter the title of the book: ")
    author = input_valid_author()
    year_published = input_valid_year()
    genre = input_valid_genre()

    book = Book(title, author, year_published, genre)
    bookshelf.add_book(book)
    book_detail = (book.title, book.author, book.year_published, book.genre)
    add_book_to_shelf(conn, book_detail)

    print("Book added successfully!")

# Function to remove a book using user input
def remove_book_menu():
    title = input("Enter the title of the book you want to remove: ")
    for book in bookshelf.get_all_books():
        if book.title == title:
            bookshelf.remove_book(book)
            delete_book_from_shelf(conn, title)
            print("Book removed successfully!")
            return
    print("Book not found in the bookshelf.")

# Function to update a book using user input
def update_book_menu():
    title = input("Enter the title of the book you want to update: ")
    for book in bookshelf.get_all_books():
        if book.title == title:
            new_title = input("Enter the new title of the book: ")
            new_author = input_valid_author()
            new_year_published = input_valid_year()
            new_genre = input_valid_genre()

            book.title = new_title
            book.author = new_author
            book.year_published = new_year_published
            book.genre = new_genre

            update_book_in_shelf(conn, title, (new_title, new_author, new_year_published, new_genre))
            print("Book updated successfully!")
            return
    print("Book not found in the bookshelf.")

# Function to search books by title in the database
def search_books_by_title(conn, title):
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM Bookshelf WHERE title=?", (title,))
        rows = c.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No books found with the title:", title)
    except Error as e:
        print("Error searching books by title:", e)

# Function to search books by author in the database
def search_books_by_author(conn, author):
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM Bookshelf WHERE author=?", (author,))
        rows = c.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No books found by author:", author)
    except Error as e:
        print("Error searching books by author:", e)

# Function to search books by genre in the database
def search_books_by_genre(conn, genre):
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM Bookshelf WHERE genre=?", (genre,))
        rows = c.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No books found in genre:", genre)
    except Error as e:
        print("Error searching books by genre:", e)

# Function to display the search menu for searching books by title, author, or genre.
def search_books_menu():
    print("Search books by:")
    print("1. Title")
    print("2. Author")
    print("3. Genre")
    search_choice = input("Enter your choice: ")
    if search_choice == "1":
        title = input("Enter the title of the book: ")
        search_books_by_title(conn, title)
    elif search_choice == "2":
        author = input_valid_author()
        search_books_by_author(conn, author)
    elif search_choice == "3":
        genre = input_valid_genre()
        search_books_by_genre(conn, genre)
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
        search_books_menu()

# Function to view all books in the bookshelf
def view_books_menu():
    print("All books in the bookshelf:")
    get_all_books_from_shelf(conn)

# Main function
if __name__ == '__main__':
    conn = create_connection()
    if conn is not None:
        create_bookshelf_table(conn)
    
    bookshelf = Bookshelf()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book_menu()
        elif choice == "2":
            remove_book_menu()
        elif choice == "3":
            update_book_menu()
        elif choice == "4":
            search_books_menu()
        elif choice == "5":
            view_books_menu()
        elif choice == "6":
            print("Exiting the Bookshelf Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
