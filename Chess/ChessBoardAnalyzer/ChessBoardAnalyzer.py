class ChessPiece:
    def __init__(self, color):
        # Initialize the piece with its color (white or black)
        self.color = color

    def get_legal_moves(self, board, position):
        # This method should be implemented by subclasses
        raise NotImplementedError("This method should be implemented by subclasses")

class King(ChessPiece):
    def get_legal_moves(self, board, position):
        # Get all legal moves for the king
        legal_moves = []
        row, col = position
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for d in directions:
            new_row, new_col = row + d[0], col + d[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] is None or board[new_row][new_col].color != self.color:
                    legal_moves.append((new_row, new_col))
        return legal_moves

class Queen(ChessPiece):
    def get_legal_moves(self, board, position):
        # Get all legal moves for the queen (straight and diagonal)
        return self.get_straight_moves(board, position) + self.get_diagonal_moves(board, position)

    def get_straight_moves(self, board, position):
        # Get all straight moves (like a rook)
        legal_moves = []
        row, col = position
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for d in directions:
            for i in range(1, 8):
                new_row, new_col = row + i * d[0], col + i * d[1]
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if board[new_row][new_col] is None:
                        legal_moves.append((new_row, new_col))
                    elif board[new_row][new_col].color != self.color:
                        legal_moves.append((new_row, new_col))
                        break
                    else:
                        break
        return legal_moves

    def get_diagonal_moves(self, board, position):
        # Get all diagonal moves (like a bishop)
        legal_moves = []
        row, col = position
        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        for d in directions:
            for i in range(1, 8):
                new_row, new_col = row + i * d[0], col + i * d[1]
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if board[new_row][new_col] is None:
                        legal_moves.append((new_row, new_col))
                    elif board[new_row][new_col].color != self.color:
                        legal_moves.append((new_row, new_col))
                        break
                    else:
                        break
        return legal_moves

class Rook(ChessPiece):
    def get_legal_moves(self, board, position):
        # Get all legal moves for the rook (straight moves)
        return Queen.get_straight_moves(self, board, position)

class Bishop(ChessPiece):
    def get_legal_moves(self, board, position):
        # Get all legal moves for the bishop (diagonal moves)
        return Queen.get_diagonal_moves(self, board, position)

class Knight(ChessPiece):
    def get_legal_moves(self, board, position):
        # Get all legal moves for the knight
        legal_moves = []
        row, col = position
        directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for d in directions:
            new_row, new_col = row + d[0], col + d[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] is None or board[new_row][new_col].color != self.color:
                    legal_moves.append((new_row, new_col))
        return legal_moves

class Pawn(ChessPiece):
    def get_legal_moves(self, board, position):
        # Get all legal moves for the pawn
        legal_moves = []
        row, col = position
        direction = 1 if self.color == 'white' else -1
        start_row = 6 if self.color == 'white' else 1
        # Forward moves
        if 0 <= row + direction < 8 and board[row + direction][col] is None:
            legal_moves.append((row + direction, col))
            if row == start_row and board[row + 2 * direction][col] is None:
                legal_moves.append((row + 2 * direction, col))
        # Capture moves
        for d_col in [-1, 1]:
            if 0 <= row + direction < 8 and 0 <= col + d_col < 8:
                if board[row + direction][col + d_col] and board[row + direction][col + d_col].color != self.color:
                    legal_moves.append((row + direction, col + d_col))
        return legal_moves

class ChessBoard:
    def __init__(self):
        # Initialize the board and set the current turn to white
        self.board = self.initialize_board()
        self.current_turn = 'white'

    def initialize_board(self):
        # Set up the initial chessboard with pieces
        board = [[None for _ in range(8)] for _ in range(8)]
        # Place pawns
        for col in range(8):
            board[1][col] = Pawn('black')
            board[6][col] = Pawn('white')
        # Place rooks
        board[0][0] = board[0][7] = Rook('black')
        board[7][0] = board[7][7] = Rook('white')
        # Place knights
        board[0][1] = board[0][6] = Knight('black')
        board[7][1] = board[7][6] = Knight('white')
        # Place bishops
        board[0][2] = board[0][5] = Bishop('black')
        board[7][2] = board[7][5] = Bishop('white')
        # Place queens
        board[0][3] = Queen('black')
        board[7][3] = Queen('white')
        # Place kings
        board[0][4] = King('black')
        board[7][4] = King('white')
        return board

    def display(self):
        # Display the board with piece abbreviations
        for row in self.board:
            print(' '.join([piece.__class__.__name__[0] if piece else '.' for piece in row]))

    def move_piece(self, start_pos, end_pos):
        # Move a piece from start_pos to end_pos if the move is legal
        piece = self.board[start_pos[0]][start_pos[1]]
        if piece and end_pos in piece.get_legal_moves(self.board, start_pos):
            self.board[end_pos[0]][end_pos[1]] = piece
            self.board[start_pos[0]][start_pos[1]] = None
            self.current_turn = 'black' if self.current_turn == 'white' else 'white'
        else:
            print("Invalid move")

    def is_check(self, color):
        # Implement check detection logic (to be completed)
        pass

    def is_checkmate(self, color):
        # Implement checkmate detection logic (to be completed)
        pass

    def generate_legal_moves(self, color):
        # Generate all legal moves for the specified color
        legal_moves = []
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.color == color:
                    legal_moves.extend(piece.get_legal_moves(self.board, (row, col)))
        return legal_moves

    def evaluate_position(self):
        # Evaluate the board position and return a score
        score = 0
        piece_values = {'K': 0, 'Q': 9, 'R': 5, 'B': 3, 'N': 3, 'P': 1}
        for row in self.board:
            for piece in row:
                if piece:
                    value = piece_values[piece.__class__.__name__[0]]
                    score += value if piece.color == 'white' else -value
        return score

if __name__ == "__main__":
    chess_board = ChessBoard()
    chess_board.display()
    # Example moves
    print("\nMaking a move:")
    # Move white pawn from e2 to e4
    chess_board.move_piece((6, 4), (4, 4))  
    chess_board.display()
    print("\nMaking a move:")
    # Move black pawn from e7 to e5
    chess_board.move_piece((1, 4), (3, 4))  
    chess_board.display()
    print("\nEvaluating position:")
    print(chess_board.evaluate_position())
    print("\nGenerating legal moves for white:")
    print(chess_board.generate_legal_moves('white'))
