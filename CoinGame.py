class CoinGame:
    def __init__(self, total_coins):
        # Initialize the game with a given number of total coins
        self.total_coins = total_coins

    def player_move(self):
        # Get the player's move
        while True:
            try:
                coins_taken = int(input(f"How many coins do you want to take (1-3)? "))
                if 1 <= coins_taken <= 3 and coins_taken <= self.total_coins:
                    return coins_taken
                else:
                    print("Invalid number of coins. You can take 1 to 3 coins.")
            except ValueError:
                print("Please enter a valid integer.")

    def ai_move(self):
        # AI decides how many coins to take using Minimax
        best_move = self.minimax(self.total_coins)
        print(f"AI takes {best_move} coin(s).")
        return best_move

    def minimax(self, coins_left):
        # Minimax algorithm to determine the best move for AI
        if coins_left <= 0:
            return 0

        best_value = -float('inf')
        best_move = 0

        # Explore all possible moves (taking 1, 2, or 3 coins)
        for move in range(1, 4):
            if coins_left - move >= 0:
                value = self.minimax(coins_left - move)
                if value < 0:  # If opponent is left with no winning moves
                    return move
                if value > best_value:
                    best_value = value
                    best_move = move

        return best_move

    def play_game(self):
        # Main game loop
        while self.total_coins > 0:
            print(f"\nCoins left: {self.total_coins}")
            # Player's turn
            coins_taken = self.player_move()
            self.total_coins -= coins_taken
            
            if self.total_coins <= 0:
                print("You took the last coin! You win!")
                break
            
            # AI's turn
            ai_taken = self.ai_move()
            self.total_coins -= ai_taken
            
            if self.total_coins <= 0:
                print("AI took the last coin! AI wins!")
                break


if __name__ == "__main__":
    # Start the game with a specified number of total coins
    total_coins = int(input("Enter the total number of coins: "))
    game = CoinGame(total_coins)
    game.play_game()
