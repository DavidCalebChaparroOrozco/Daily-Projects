# Recursively calculates the number of ways to tile a 2xN board using 2x1 tiles.
def tiling_problem(n):
    """    
    n: The length of the board (2xN).
    return: The number of ways to tile the board.
    """
    # Base cases
    if n == 0:
        return 1  # One way to tile a board of size 2x0 (empty board)
    if n == 1:
        return 1  # Only one way to tile a 2x1 board (one vertical tile)

    # Recursive case: 
    # We can place one vertical tile (then solve for the remaining 2x(N-1) board)
    # or two horizontal tiles stacked (then solve for the remaining 2x(N-2) board)
    return tiling_problem(n - 1) + tiling_problem(n - 2)

def main():
    # Input: length of the board
    n = int(input("Enter the length of the board (N) for a 2xN board: "))
    
    # Calculate the number of ways to tile the board
    ways = tiling_problem(n)
    
    # Output the result
    print(f"The number of ways to tile a 2x{n} board is: {ways}")

if __name__ == "__main__":
    main()
