class ArtPiece:
    def __init__(self, art_id, title, artist, price, stock):
        self.art_id = art_id
        self.title = title
        self.artist = artist
        self.price = price
        self.stock = stock

    def __str__(self):
        return f'{self.title} by {self.artist} - ${self.price} ({self.stock} in stock)'


class Inventory:
    def __init__(self):
        self.art_pieces = []

    def add_art_piece(self, art_piece):
        self.art_pieces.append(art_piece)

    def remove_art_piece(self, art_id):
        for art in self.art_pieces:
            if art.art_id == art_id:
                self.art_pieces.remove(art)
                return True
        return False

    def get_all_art_pieces(self):
        return self.art_pieces

    def get_art_piece_by_id(self, art_id):
        for art in self.art_pieces:
            if art.art_id == art_id:
                return art
        return None
