from controller.controller import Controller
from view.view import View

# Main entry point of the application
if __name__ == "__main__":
    controller = Controller()
    
    # Adding some authors and books
    controller.add_author("J.K. Rowling", "A001")
    controller.add_author("George R.R. Martin", "A002")
    controller.add_author("H. P. Lovecraft", "A003")
    controller.add_author("Antoine de Saint-Exupéry", "A004")
    
    controller.add_book("Harry Potter", "Fantasy", "A001", 9.3, 500)
    controller.add_book("Game of Thrones", "Fantasy", "A002", 8.9, 800)
    controller.add_book("The Cats of Ulthar", "Horror", "A003", 8.9, 57)
    controller.add_book("The Little Prince", "Fable", "A004", 9.0, 109)

    while True:
        option = View.display_menu()

        if option == "1":
            reader_name = View.get_input("Enter reader name: ")
            reader_id = View.get_input("Enter reader ID: ")
            genre = View.get_input("Enter genre to subscribe (Fantasy/Adventure/Horror/Fable): ")
            controller.subscribe_reader_to_genre(reader_id, reader_name, genre)

        elif option == "2":
            reader_id = View.get_input("Enter reader ID: ")
            controller.display_reader_details(reader_id)

        elif option == "3":
            book_title = View.get_input("Enter book title (Harry Potter/Game of Thrones/The Cats of Ulthar/The Little Prince): ")
            controller.display_book_details(book_title)

        elif option == "4":
            break

        else:
            View.show_message("Invalid option. Please try again.")
