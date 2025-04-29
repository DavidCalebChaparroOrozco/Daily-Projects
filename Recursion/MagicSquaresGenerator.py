# Import necessary libraries
import numpy as np

class MagicSquareGenerator:
    # Initialize the MagicSquareGenerator with a given size.
    def __init__(self, size):
        """    
        Args:
            size: The size of the magic square (NxN grid).
        """
        self.size = size
        # The magic constant
        self.magic_sum = size * (size**2 + 1) // 2  
        # Initialize grid with zeros
        self.grid = np.zeros((size, size), dtype=int)  
        # Track used numbers to avoid duplicates
        self.used_numbers = set()  
        
    # Check if placing a number at a given position is valid.
    def is_valid(self, row, col, num):
        """
        Args:
            row: Row index.
            col: Column index.
            num: Number to be placed.
        Returns:
            bool: True if the placement is valid, False otherwise.
        """
        # Check if the number is already used
        if num in self.used_numbers:
            return False
            
        # Place the number temporarily
        self.grid[row, col] = num
        
        # Check row completeness and sum
        # If row is complete
        if np.all(self.grid[row, :] != 0):  
            if np.sum(self.grid[row, :]) != self.magic_sum:
                # Undo placement
                self.grid[row, col] = 0  
                return False
                
        # Check column completeness and sum
        # If column is complete
        if np.all(self.grid[:, col] != 0):  
            if np.sum(self.grid[:, col]) != self.magic_sum:
                # Undo placement
                self.grid[row, col] = 0  
                return False
                
        # Check main diagonal (top-left to bottom-right) if position is on it
        if row == col:
            # If diagonal is complete
            if np.all(np.diag(self.grid) != 0):  
                if np.sum(np.diag(self.grid)) != self.magic_sum:
                    # Undo placement
                    self.grid[row, col] = 0  
                    return False
                    
        # Check anti-diagonal (top-right to bottom-left) if position is on it
        if row + col == self.size - 1:
            if np.all(np.diag(np.fliplr(self.grid)) != 0):  # If anti-diagonal is complete
                if np.sum(np.diag(np.fliplr(self.grid))) != self.magic_sum:
                    # Undo placement
                    self.grid[row, col] = 0  
                    return False
                    
        # Undo temporary placement (actual placement happens in solve())
        self.grid[row, col] = 0
        return True
        
    # Recursive function to solve the magic square using backtracking.
    def solve(self, row=0, col=0):
        """    
        Args:
            row: Current row index.
            col: Current column index.
            
        Returns:
            bool: True if a solution is found, False otherwise.
        """
        # Base case: If all cells are filled, return True
        if row == self.size - 1 and col == self.size:
            return True
            
        # Move to next row if column limit is reached
        if col == self.size:
            row += 1
            col = 0
            
        # Skip already filled cells
        if self.grid[row, col] != 0:
            return self.solve(row, col + 1)
            
        # Try numbers from 1 to N^2
        for num in range(1, self.size**2 + 1):
            if self.is_valid(row, col, num):
                # Place the number
                self.grid[row, col] = num
                self.used_numbers.add(num)
                
                # Recur to place next number
                if self.solve(row, col + 1):
                    return True
                    
                # Backtrack if placement doesn't lead to solution
                self.grid[row, col] = 0
                self.used_numbers.remove(num)
                
        return False
        
    # Generate and return a magic square if possible.
    def generate_magic_square(self):
        """    
        Returns:
            numpy.ndarray: The magic square grid if found, None otherwise.
        """
        if self.solve():
            return self.grid
        else:
            print(f"No magic square found for size {self.size}")
            return None
            
    # Print the magic square in a readable format.
    def print_magic_square(self):
        if self.grid is not None:
            print(f"\n{self.size}x{self.size} Magic Square (Magic Sum: {self.magic_sum}):")
            print("=".center(40, "="))
            for row in self.grid:
                print(" | ".join(f"{num:3d}" for num in row))
            print("=".center(40, "="))
        else:
            print("No magic square to display.")

# Main function to get user input and generate magic squares.
def main():
    print("Magic Squares Generator by David Caleb")
    print("=".center(40, "="))
    
    while True:
        try:
            size = int(input("\nEnter the size of the magic square (N >= 3): "))
            if size < 3:
                print("Size must be at least 3.")
                continue
                
            generator = MagicSquareGenerator(size)
            magic_square = generator.generate_magic_square()
            
            if magic_square is not None:
                generator.print_magic_square()
                
            another = input("\nGenerate another magic square? (y/n): ").lower()
            if another != 'y':
                break
                
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()