class ChessBoard:
    def __init__(self):
        # Initialize the standard 8x8 chess board with pieces in starting positions
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]

    def display_board(self, highlight=None):
        # Display the chess board in console
        # If 'highlight' is provided, mark those positions (e.g., legal moves)
        print("\n    a b c d e f g h")
        print("=".center(20, "="))
        for row in range(8):
            print(f"{8 - row} |", end=" ")
            for col in range(8):
                if highlight and (row, col) in highlight:
                    if self.board[row][col] == '.':
                        # Highlight empty squares
                        print('*', end=" ")  
                    else:
                        # Show piece on highlight square
                        print(self.board[row][col], end=" ")  
                else:
                    print(self.board[row][col], end=" ")
            print(f"| {8 - row}")
        print("=".center(20, "="))
        print("    a b c d e f g h\n")

    def get_piece_at(self, position):
        # Return the piece located at the given board position (e.g., "e2")
        if len(position) != 2:
            return None
        col = ord(position[0].lower()) - ord('a')
        row = 8 - int(position[1])
        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]
        return None

    def get_legal_moves(self, position):
        # Return a list of legal moves for the piece at the given position
        piece = self.get_piece_at(position)
        if not piece or piece == '.':
            return []

        col = ord(position[0].lower()) - ord('a')
        row = 8 - int(position[1])
        moves = []

        piece_lower = piece.lower()

        if piece_lower == 'p':
            # Pawn logic (handle direction and captures)
            direction = -1 if piece.isupper() else 1
            start_row = 6 if piece.isupper() else 1

            # Forward move
            if self._is_valid_square(row + direction, col) and self.board[row + direction][col] == '.':
                moves.append((row + direction, col))

                # Double move from starting position
                if row == start_row and self.board[row + 2*direction][col] == '.':
                    moves.append((row + 2*direction, col))

            # Diagonal captures
            for dc in [-1, 1]:
                new_row, new_col = row + direction, col + dc
                if self._is_valid_square(new_row, new_col):
                    target = self.board[new_row][new_col]
                    if target != '.' and ((piece.isupper() and target.islower()) or (piece.islower() and target.isupper())):
                        moves.append((new_row, new_col))

        elif piece_lower == 'n':
            # Knight logic (8 possible L-shaped moves)
            knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                            (1, -2), (1, 2), (2, -1), (2, 1)]
            for dr, dc in knight_moves:
                new_row, new_col = row + dr, col + dc
                if self._is_valid_square(new_row, new_col):
                    target = self.board[new_row][new_col]
                    if target == '.' or ((piece.isupper() and target.islower()) or (piece.islower() and target.isupper())):
                        moves.append((new_row, new_col))

        elif piece_lower == 'b':
            # Bishop logic (diagonal movement)
            moves.extend(self._get_diagonal_moves(row, col, piece))

        elif piece_lower == 'r':
            # Rook logic (straight movement)
            moves.extend(self._get_straight_moves(row, col, piece))

        elif piece_lower == 'q':
            # Queen logic (diagonal + straight)
            moves.extend(self._get_diagonal_moves(row, col, piece))
            moves.extend(self._get_straight_moves(row, col, piece))

        elif piece_lower == 'k':
            # King logic (one square in any direction)
            king_moves = [(-1, -1), (-1, 0), (-1, 1),
                            (0, -1),          (0, 1),
                            (1, -1),  (1, 0), (1, 1)]
            for dr, dc in king_moves:
                new_row, new_col = row + dr, col + dc
                if self._is_valid_square(new_row, new_col):
                    target = self.board[new_row][new_col]
                    if target == '.' or ((piece.isupper() and target.islower()) or (piece.islower() and target.isupper())):
                        moves.append((new_row, new_col))

        return moves

    def _is_valid_square(self, row, col):
        # Check if a position is within the bounds of the board
        return 0 <= row < 8 and 0 <= col < 8

    def _get_diagonal_moves(self, row, col, piece):
        # Return list of valid diagonal moves for bishops or queens
        moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            while self._is_valid_square(new_row, new_col):
                target = self.board[new_row][new_col]
                if target == '.':
                    moves.append((new_row, new_col))
                else:
                    if (piece.isupper() and target.islower()) or (piece.islower() and target.isupper()):
                        moves.append((new_row, new_col))
                    break
                new_row += dr
                new_col += dc
        return moves

    def _get_straight_moves(self, row, col, piece):
        # Return list of valid horizontal and vertical moves for rooks or queens
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            while self._is_valid_square(new_row, new_col):
                target = self.board[new_row][new_col]
                if target == '.':
                    moves.append((new_row, new_col))
                else:
                    if (piece.isupper() and target.islower()) or (piece.islower() and target.isupper()):
                        moves.append((new_row, new_col))
                    break
                new_row += dr
                new_col += dc
        return moves


def main():
    # Main program loop
    print(" Chess Legal Move Highlighter by David Caleb ".center(50, "="))
    board = ChessBoard()

    while True:
        board.display_board()
        user_input = input("Enter piece position (e.g., 'e2') or 'quit': ").strip().lower()

        if user_input == 'quit':
            print("Exiting... Goodbye!")
            break

        # Validate input
        if len(user_input) != 2 or user_input[0] not in "abcdefgh" or user_input[1] not in "12345678":
            print("❌ Invalid input. Use format like 'e2'.")
            continue

        piece = board.get_piece_at(user_input)
        if not piece or piece == '.':
            print(f"No piece found at {user_input.upper()}. Try another square.")
            continue

        # Get and display legal moves
        legal_moves = board.get_legal_moves(user_input)
        print(f"\nLegal moves for {piece} at {user_input.upper()}:")

        if not legal_moves:
            print("⚠️  No legal moves available for this piece.")
        else:
            board.display_board(highlight=legal_moves)

            # Display moves in algebraic notation
            algebraic_moves = []
            for row, col in legal_moves:
                file = chr(col + ord('a'))
                rank = 8 - row
                algebraic_moves.append(f"{file}{rank}")
            print("Algebraic Notation:", ', '.join(algebraic_moves))
        print()


if __name__ == "__main__":
    main()
