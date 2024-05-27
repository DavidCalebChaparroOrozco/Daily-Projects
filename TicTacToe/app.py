import socket
import threading

class TicTacToe:

    def __init__(self):
        # Initialize the game board, turn, player symbols, winner, game over status, and move counter
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turn = "X"
        self.you = "X"
        self.opponent = "0"
        self.winner = None
        self.game_over = None
        self.counter = 0

    def host_game(self, host, port):
        # Set up the server to host the game
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(1)

        # Accept a connection from a client
        client, addr = server.accept()

        # Set player symbols
        self.you = "X"
        self.opponent = "0"
        
        # Handle the connection in a separate thread
        threading.Thread(target=self.handle_connection, args=(client,)).start()
        server.close()

    def connect_to_game(self, host, port):
        # Connect to an existing game as a client
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))

        # Set player symbols
        self.you = '0'
        self.opponent = 'X'
        
        # Handle the connection in a separate thread
        threading.Thread(target=self.handle_connection, args=(client,)).start()

    def handle_connection(self, client):
        # Handle communication with the connected player
        while not self.game_over:
            if self.turn == self.you:
                # If it's the player's turn, get their move
                move = input("Enter a move (row, column): ")
                if self.check_valid_move(move.split(',')):
                    # Send the move to the opponent
                    client.send(move.encode('utf-8'))
                    # Apply the move locally
                    self.apply_move(move.split(','), self.you)
                    # Switch turn to the opponent
                    self.turn = self.opponent
                else:
                    print("Invalid Move!")
            else:
                # If it's the opponent's turn, receive their move
                data = client.recv(1024)
                if not data:
                    break
                else:
                    # Apply the opponent's move locally
                    self.apply_move(data.decode('utf-8').split(','), self.opponent)
                    # Switch turn to the player
                    self.turn = self.you
        client.close()

    def apply_move(self, move, player):
        # Apply a move to the board
        if self.game_over:
            return
        self.counter += 1
        self.board[int(move[0])][int(move[1])] = player
        self.print_board()
        if self.check_if_won():
            if self.winner == self.you:
                print("You win!!")
                exit()
            elif self.winner == self.opponent:
                print("You lose!")
                exit()
        else:
            if self.counter == 9:
                print("It's a tie!")
                exit()

    def check_valid_move(self, move):
        # Check if a move is valid (i.e., the cell is empty)
        return self.board[int(move[0])][int(move[1])] == " "

    def check_if_won(self):
        # Check if there is a winning condition on the board
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                self.winner = self.board[row][0]
                self.game_over = True
                return True

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                self.winner = self.board[0][col]
                self.game_over = True
                return True
            
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            self.winner = self.board[0][0]
            self.game_over = True
            return True
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            self.winner = self.board[0][2]
            self.game_over = True
            return True
        
        return False

    def print_board(self):
        # Print the current state of the board
        print("")
        for row in range(3):
            print(" | ".join(self.board[row]))
            if row != 2:
                print("-----------")

# Start a game as a client connecting to a host
game = TicTacToe()
game.host_game("localhost", 9999)