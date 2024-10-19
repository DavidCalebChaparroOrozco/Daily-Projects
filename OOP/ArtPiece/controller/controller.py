from model.model import Inventory, ArtPiece
from view.view import ArtStoreView

class ArtStoreController:
    def __init__(self):
        self.inventory = Inventory()
        self.view = ArtStoreView()

    def run(self):
        while True:
            self.view.display_menu()
            choice = input("Select an option: ")

            if choice == '1':
                self.view.display_art_pieces(self.inventory.get_all_art_pieces())
            elif choice == '2':
                self.add_art_piece()
            elif choice == '3':
                self.remove_art_piece()
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                self.view.display_error_message("Invalid option, try again.")

    def add_art_piece(self):
        art_id, title, artist, price, stock = self.view.get_art_piece_details()
        art_piece = ArtPiece(art_id, title, artist, price, stock)
        self.inventory.add_art_piece(art_piece)
        self.view.display_success_message(f'Added {title} by {artist}')

    def remove_art_piece(self):
        art_id = self.view.get_art_piece_id()
        if self.inventory.remove_art_piece(art_id):
            self.view.display_success_message(f'Removed art piece with ID: {art_id}')
        else:
            self.view.display_error_message(f'Art piece with ID {art_id} not found.')
