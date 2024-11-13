# Class representing a chess piece."""
class ChessPiece:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def __str__(self):
        return f"{self.color[0].upper()}{self.name[0].upper()}"  # E.g., 'wP' for white pawn


# Class representing the chess board.
class ChessBoard:
    def __init__(self):
        self.board = self.create_board()

    # Initialize the chessboard with pieces.
    def create_board(self):
        board = [[None] * 8 for _ in range(8)]
        # Set up pawns
        for i in range(8):
            board[1][i] = ChessPiece('white', 'pawn')
            board[6][i] = ChessPiece('black', 'pawn')
        # Set up other pieces
        pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
        for i, piece in enumerate(pieces):
            board[0][i] = ChessPiece('white', piece)
            board[7][i] = ChessPiece('black', piece)
        return board

    # Display the chessboard.
    def display(self):
        for row in self.board:
            print(" ".join([str(piece) if piece else "--" for piece in row]))
        print()

    # Move a piece from start to end position.
    def move_piece(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        piece = self.board[start_row][start_col]

        if piece and self.is_valid_move(start, end):
            self.board[end_row][end_col] = piece
            self.board[start_row][start_col] = None
            return True
        return False

    # Basic validation of moves (to be expanded).
    def is_valid_move(self, start, end):
        # For simplicity, we only check if the destination is empty or has an opponent's piece.
        start_row, start_col = start
        end_row, end_col = end
        piece = self.board[start_row][start_col]

        if not piece:
            return False  # No piece to move

        target_piece = self.board[end_row][end_col]
        
        if target_piece and target_piece.color == piece.color:
            return False  # Can't capture own piece
        
        return True  # Basic validation passed


# Main function to run the chess game.
def main():
    board = ChessBoard()
    current_player = 'white'

    while True:
        board.display()
        
        print(f"{current_player.capitalize()}'s turn.")
        
        try:
            start_input = input("Enter the position of the piece to move (e.g., '1 0'): ")
            end_input = input("Enter the position to move to (e.g., '2 0'): ")
            
            start_pos = tuple(map(int, start_input.split()))
            end_pos = tuple(map(int, end_input.split()))

            if board.move_piece(start_pos, end_pos):
                current_player = 'black' if current_player == 'white' else 'white'
            else:
                print("Invalid move. Try again.")
        
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid coordinates.")

if __name__ == "__main__":
    main()