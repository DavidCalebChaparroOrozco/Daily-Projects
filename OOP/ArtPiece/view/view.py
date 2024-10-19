class ArtStoreView:
    @staticmethod
    def display_menu():
        print("\nWelcome to the Art Store")
        print("1. View all art pieces")
        print("2. Add new art piece")
        print("3. Remove art piece")
        print("4. Exit")

    @staticmethod
    def display_art_pieces(art_pieces):
        if not art_pieces:
            print("No art pieces available.")
        else:
            for art in art_pieces:
                print(art)

    @staticmethod
    def get_art_piece_details():
        art_id = input("Enter Art ID: ")
        title = input("Enter Art Title: ")
        artist = input("Enter Artist: ")
        price = float(input("Enter Price: "))
        stock = int(input("Enter Stock: "))
        return art_id, title, artist, price, stock

    @staticmethod
    def get_art_piece_id():
        return input("Enter the Art ID to remove: ")

    @staticmethod
    def display_success_message(message):
        print(f"Success: {message}")

    @staticmethod
    def display_error_message(message):
        print(f"Error: {message}")
