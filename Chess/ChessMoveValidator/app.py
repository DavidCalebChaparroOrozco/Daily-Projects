class ChessBoard:
    def __init__(self):
        # Initialize the board and other settings
        self.board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]
        self.castling_rights = {'K': True, 'Q': True, 'k': True, 'q': True}  # Castling availability
        self.en_passant_target = None  # En passant target square

    # Validates if a move is legal and returns the move description.
    def is_move_legal(self, move, player):
        """
        Args:
            move (tuple): The move represented as (start_pos, end_pos).
            player (str): The current player ('white' or 'black').
        
        Returns:
            bool: True if the move is legal, False otherwise.
            str: Description of the move if legal, or a failure message.
        """
        start_pos, end_pos = move
        piece = self.get_piece_at(start_pos)
        
        if not piece:
            return False, "No piece at starting position."
        
        if not self.is_correct_player(piece, player):
            return False, "The piece does not belong to the current player."
        
        if not self.is_valid_move_for_piece(piece, start_pos, end_pos):
            return False, "Invalid move for this piece."
        
        if self.is_in_check_after_move(start_pos, end_pos, player):
            return False, "Move leaves player in check."
        
        move_description = self.describe_move(piece, start_pos, end_pos)
        self.make_move(start_pos, end_pos)
        return True, move_description

    # Get the piece at a given position (row, col). 
    def get_piece_at(self, position):
        row, col = position
        return self.board[row][col]

    # Check if the piece belongs to the correct player.
    def is_correct_player(self, piece, player):
        if player == 'white' and piece.isupper():
            return True
        if player == 'black' and piece.islower():
            return True
        return False

    # Check if the move is valid for the specific piece.
    def is_valid_move_for_piece(self, piece, start_pos, end_pos):
        row_start, col_start = start_pos
        row_end, col_end = end_pos
        
        if piece.lower() == 'p':  # Pawn
            return self.is_valid_pawn_move(piece, start_pos, end_pos)
        if piece.lower() == 'r':  # Rook
            return self.is_valid_rook_move(start_pos, end_pos)
        if piece.lower() == 'n':  # Knight
            return self.is_valid_knight_move(start_pos, end_pos)
        if piece.lower() == 'b':  # Bishop
            return self.is_valid_bishop_move(start_pos, end_pos)
        if piece.lower() == 'q':  # Queen
            return self.is_valid_queen_move(start_pos, end_pos)
        if piece.lower() == 'k':  # King
            return self.is_valid_king_move(start_pos, end_pos)
        
        return False  # Invalid piece or move

    # Validate pawn movement.
    def is_valid_pawn_move(self, piece, start_pos, end_pos):
        row_start, col_start = start_pos
        row_end, col_end = end_pos
        direction = -1 if piece.isupper() else 1  # White pawns move up (-1), black pawns move down (+1)
        
        # Single move forward
        if col_start == col_end and self.board[row_end][col_end] == "":
            if row_end == row_start + direction:
                return True
            # Double move from starting position
            if row_end == row_start + 2 * direction and (row_start == 1 or row_start == 6):
                return True
        
        # Capture move
        if abs(col_end - col_start) == 1 and row_end == row_start + direction:
            if self.board[row_end][col_end] != "":
                return True
            # En passant
            if (row_end, col_end) == self.en_passant_target:
                return True
        
        return False

    # Validate rook movement.
    def is_valid_rook_move(self, start_pos, end_pos):
        return self.is_straight_line_move(start_pos, end_pos)

    # Validate knight movement.
    def is_valid_knight_move(self, start_pos, end_pos):
        row_diff = abs(end_pos[0] - start_pos[0])
        col_diff = abs(end_pos[1] - start_pos[1])
        return (row_diff, col_diff) in [(2, 1), (1, 2)]

    # Validate bishop movement.
    def is_valid_bishop_move(self, start_pos, end_pos):
        return self.is_diagonal_move(start_pos, end_pos)

    # Validate queen movement.
    def is_valid_queen_move(self, start_pos, end_pos):
        return self.is_straight_line_move(start_pos, end_pos) or self.is_diagonal_move(start_pos, end_pos)

    # Validate king movement.
    def is_valid_king_move(self, start_pos, end_pos):
        row_diff = abs(end_pos[0] - start_pos[0])
        col_diff = abs(end_pos[1] - start_pos[1])
        if max(row_diff, col_diff) == 1:
            return True  # Single move
        if self.is_castling_move(start_pos, end_pos):
            return True  # Castling
        return False

    # Validate straight line move.
    def is_straight_line_move(self, start_pos, end_pos):
        return start_pos[0] == end_pos[0] or start_pos[1] == end_pos[1]

    # Validate diagonal move.
    def is_diagonal_move(self, start_pos, end_pos):
        return abs(start_pos[0] - end_pos[0]) == abs(start_pos[1] - end_pos[1])

    # Validate castling move.
    def is_castling_move(self, start_pos, end_pos):
        row_start, col_start = start_pos
        row_end, col_end = end_pos
        if row_start != row_end or abs(col_end - col_start) != 2:
            return False
        return True

    # Check if move puts player in check.
    def is_in_check_after_move(self, start_pos, end_pos, player):
        # Simulate move and check for check condition
        return False

    # Describe the move in chess notation style.
    def describe_move(self, piece, start_pos, end_pos):
        """
        Args:
            piece (str): The chess piece ('P', 'K', etc.).
            start_pos (tuple): The starting position.
            end_pos (tuple): The ending position.
        
        Returns:
            str: A string describing the move.
        """
        piece_names = {
            'P': 'Pawn', 'R': 'Rook', 'N': 'Knight', 'B': 'Bishop', 'Q': 'Queen', 'K': 'King',
            'p': 'Pawn', 'r': 'Rook', 'n': 'Knight', 'b': 'Bishop', 'q': 'Queen', 'k': 'King'
        }
        
        col_names = "abcdefgh"  # Column labels for chess notation
        row_start, col_start = start_pos
        row_end, col_end = end_pos
        
        piece_name = piece_names[piece]
        start_square = f"{col_names[col_start]}{8 - row_start}"
        end_square = f"{col_names[col_end]}{8 - row_end}"
        
        return f"{piece_name} moves from {start_square} to {end_square}"

    # Updates the board with the move.
    def make_move(self, start_pos, end_pos):
        piece = self.get_piece_at(start_pos)
        self.board[end_pos[0]][end_pos[1]] = piece
        self.board[start_pos[0]][start_pos[1]] = ""

    # Print the board after each move.
    def print_board(self):
        for row in self.board:
            print(" ".join(piece if piece else "." for piece in row))
        print()

# Example usage
chess_board = ChessBoard()

# Validate a move for a white pawn from a2 to a4
move = ((6, 0), (4, 0))  # a2 to a4
is_legal, message = chess_board.is_move_legal(move, 'white')
print(f"Move is legal: {is_legal}, {message}")
chess_board.print_board()

# Validate an invalid move for a white pawn from a4 to a5
move = ((4, 0), (3, 1))  # Invalid move for pawn
is_legal, message = chess_board.is_move_legal(move, 'white')
print(f"Move is legal: {is_legal}, {message}")
chess_board.print_board()


# The black knight moves from b8 to a6
move = ((0, 1), (2, 0))  
is_legal, message = chess_board.is_move_legal(move, 'black')
print(f"Move is legal: {is_legal}, {message}")
chess_board.print_board()
