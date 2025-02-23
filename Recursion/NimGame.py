# Solves the Nim game using recursion with memoization for optimization.
def nim_game_solver(piles, player=1, memo={}):
    """
    piles: A list of integers representing the number of objects in each pile.
    player: An integer representing the current player (1 for Player 1, -1 for Player 2).
    memo: A dictionary to store already computed results for optimization.
    return: The winning player (1 or -1) if both players play optimally.
    """
    
    # Convert piles to a tuple to use as a dictionary key
    key = tuple(piles), player
    
    # Check if the result is already computed
    if key in memo:
        return memo[key]
    
    # Base case: If all piles are empty, the current player loses.
    if all(pile == 0 for pile in piles):
        memo[key] = -player
        return memo[key]
    
    # Iterate through each pile
    for i in range(len(piles)):
        # Check if the current pile has objects to remove
        if piles[i] > 0:
            # Try removing 1 to all objects from the current pile
            for j in range(1, piles[i] + 1):
                # Make a move by removing j objects from the i-th pile
                piles[i] -= j
                
                # Recursively call the function for the next player
                result = nim_game_solver(piles, -player, memo)
                
                # Undo the move to backtrack
                piles[i] += j
                
                # If the current player can force a win, return the current player
                if result == player:
                    memo[key] = player
                    return memo[key]
    
    # If no move leads to a win for the current player, the other player wins
    memo[key] = -player
    return memo[key]

# Prints the current state of the piles.
def print_game_state(piles):
    print("Current piles:", piles)

# Allows the player to make a move.
def player_turn(piles):
    print_game_state(piles)
    while True:
        try:
            pile = int(input("Choose a pile (1 to {}): ".format(len(piles)))) - 1
            if pile < 0 or pile >= len(piles) or piles[pile] == 0:
                print("Invalid pile. Try again.")
                continue
            objects = int(input("Choose the number of objects to remove (1 to {}): ".format(piles[pile])))
            if objects < 1 or objects > piles[pile]:
                print("Invalid number of objects. Try again.")
                continue
            piles[pile] -= objects
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

# Computer makes an optimal move.
def computer_turn(piles):
    print("Computer's turn...")
    original_piles = piles.copy()
    for i in range(len(piles)):
        if piles[i] > 0:
            for j in range(1, piles[i] + 1):
                piles[i] -= j
                result = nim_game_solver(piles, -1)
                piles[i] += j
                if result == -1:
                    piles[i] -= j
                    print("Computer removes {} objects from pile {}.".format(j, i + 1))
                    return
    # If no winning move, make a random move
    for i in range(len(piles)):
        if piles[i] > 0:
            piles[i] -= 1
            print("Computer removes 1 object from pile {}.".format(i + 1))
            return

# Main function to play the Nim game.
def play_nim_game():
    print("Welcome to the Nim Game!")
    print("Rules: Players take turns removing objects from piles. The player to remove the last object loses.")
    
    # Initialize piles
    while True:
        try:
            piles = list(map(int, input("Enter the number of objects in each pile (separated by spaces): ").split()))
            if all(pile >= 0 for pile in piles):
                break
            else:
                print("Piles must have non-negative objects. Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers separated by spaces.")
    
    # Decide who starts
    while True:
        starter = input("Who starts? (player/computer): ").lower()
        if starter in ["player", "computer"]:
            break
        else:
            print("Invalid choice. Please enter 'player' or 'computer'.")
    
    current_player = "player" if starter == "player" else "computer"
    
    # Game loop
    while True:
        if current_player == "player":
            player_turn(piles)
            if all(pile == 0 for pile in piles):
                print("Player removes the last object. Computer wins!")
                break
            current_player = "computer"
        else:
            computer_turn(piles)
            if all(pile == 0 for pile in piles):
                print("Computer removes the last object. Player wins!")
                break
            current_player = "player"

# Example usage:
if __name__ == "__main__":
    play_nim_game()