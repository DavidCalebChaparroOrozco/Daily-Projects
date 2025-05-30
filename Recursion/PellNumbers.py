# Import necessary libraries
import time
import matplotlib.pyplot as plt
import sys
from typing import List, Optional

# A class to generate and work with Pell numbers using various methods.
class PellGenerator:
    def __init__(self):
        # Cache for memoization to optimize recursive calls
        self.cache = {0: 0, 1: 1}
    
    # Generate the nth Pell number using pure recursion.
    def pell_recursive(self, n: int) -> int:
        """        
        Args:
            n: The index of the Pell number to generate
        Returns:
            The nth Pell number
        """
        if n < 0:
            raise ValueError("Input must be a non-negative integer")
        if n == 0:
            return 0
        if n == 1:
            return 1
        return 2 * self.pell_recursive(n - 1) + self.pell_recursive(n - 2)
    
    # Generate the nth Pell number using recursion with memoization for optimization.
    def pell_memoization(self, n: int) -> int:
        """    
        Args:
            n: The index of the Pell number to generate
        Returns:
            The nth Pell number
        """
        if n < 0:
            raise ValueError("Input must be a non-negative integer")
        if n in self.cache:
            return self.cache[n]
        
        self.cache[n] = 2 * self.pell_memoization(n - 1) + self.pell_memoization(n - 2)
        return self.cache[n]
    
    # Generate the nth Pell number using an iterative approach.
    def pell_iterative(self, n: int) -> int:
        """
        Args:
            n: The index of the Pell number to generate
        Returns:
            The nth Pell number
        """
        if n < 0:
            raise ValueError("Input must be a non-negative integer")
        if n == 0:
            return 0
        if n == 1:
            return 1
            
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, 2 * b + a
        return b
    
    # Generate a sequence of Pell numbers up to the nth term.
    def generate_sequence(self, n: int, method: str = 'iterative') -> List[int]:
        """    
        Args:
            n: The number of terms to generate
            method: The generation method ('recursive', 'memoization', or 'iterative')            
        Returns:
            A list of the first n Pell numbers
        """
        if n < 0:
            raise ValueError("Input must be a non-negative integer")
            
        if method == 'recursive':
            return [self.pell_recursive(i) for i in range(n)]
        elif method == 'memoization':
            return [self.pell_memoization(i) for i in range(n)]
        elif method == 'iterative':
            return [self.pell_iterative(i) for i in range(n)]
        else:
            raise ValueError("Invalid method. Choose 'recursive', 'memoization', or 'iterative'")
    
    # Check if a number is a Pell number.
    @staticmethod
    def is_pell_number(num: int) -> bool:
        """
        Args:
            num: The number to check
        """
        if num < 0:
            return False
        if num == 0 or num == 1:
            return True
            
        a, b = 0, 1
        while b < num:
            a, b = b, 2 * b + a
        return b == num
    
    # Benchmark different Pell number generation methods for comparison.
    @staticmethod
    def benchmark(n: int) -> dict:
        """
        Args:
            n: The index to benchmark up to
            
        Returns:
            A dictionary with timing results for each method
        """
        generator = PellGenerator()
        results = {}
        
        # Test recursive method (only up to 30 to avoid excessive runtime)
        max_recursive = min(n, 30)
        start = time.time()
        generator.pell_recursive(max_recursive)
        results['recursive'] = time.time() - start
        
        # Test memoization method
        start = time.time()
        generator.pell_memoization(n)
        results['memoization'] = time.time() - start
        
        # Test iterative method
        start = time.time()
        generator.pell_iterative(n)
        results['iterative'] = time.time() - start
        
        return results
    
    # Plot a sequence of Pell numbers.
    @staticmethod
    def plot_sequence(sequence: List[int], title: Optional[str] = None) -> None:
        """    
        Args:
            sequence: The sequence of numbers to plot
            title: Optional title for the plot
        """
        plt.figure(figsize=(10, 6))
        plt.plot(sequence, marker='o', linestyle='-', color='b')
        plt.title(title or 'Pell Numbers Sequence')
        plt.xlabel('Index')
        plt.ylabel('Value')
        plt.grid(True)
        plt.show()

def display_menu() -> None:
    print("\n" + "=" * 50)
    print("PELL NUMBERS GENERATOR".center(50))
    print("=".center(50, "="))
    print("1. Generate Pell number at specific index")
    print("2. Generate sequence of Pell numbers")
    print("3. Check if a number is a Pell number")
    print("4. Compare performance of different methods")
    print("5. Visualize Pell numbers sequence")
    print("6. Learn about Pell numbers")
    print("7. Exit")
    print("=".center(50, "="))

# Get a positive integer from user input with validation.
def get_positive_integer(prompt: str) -> int:
    """    
    Args:
        prompt: The prompt to display to the user
    Returns:
        The validated positive integer
    """
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    generator = PellGenerator()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            # Generate single Pell number
            try:
                n = get_positive_integer("Enter the index of the Pell number to generate: ")
                method = input("Choose method (recursive/memoization/iterative) [default: iterative]: ").lower() or 'iterative'
                
                if method not in ['recursive', 'memoization', 'iterative']:
                    print("Invalid method. Using iterative as default.")
                    method = 'iterative'
                
                start_time = time.time()
                
                if method == 'recursive':
                    result = generator.pell_recursive(n)
                elif method == 'memoization':
                    result = generator.pell_memoization(n)
                else:
                    result = generator.pell_iterative(n)
                
                elapsed = time.time() - start_time
                
                print(f"\nPell number at index {n}: {result}")
                print(f"Generated using {method} method in {elapsed:.6f} seconds")
                
            except ValueError as e:
                print(f"Error: {e}")
            except RecursionError:
                print("Error: Recursion depth too large. Try a smaller number or use iterative/memoization method.")
        
        elif choice == '2':
            # Generate sequence
            try:
                n = get_positive_integer("Enter the number of Pell numbers to generate: ")
                method = input("Choose method (recursive/memoization/iterative) [default: iterative]: ").lower() or 'iterative'
                
                if method not in ['recursive', 'memoization', 'iterative']:
                    print("Invalid method. Using iterative as default.")
                    method = 'iterative'
                
                start_time = time.time()
                sequence = generator.generate_sequence(n, method)
                elapsed = time.time() - start_time
                
                print(f"\nFirst {n} Pell numbers:")
                print(sequence)
                print(f"\nGenerated using {method} method in {elapsed:.6f} seconds")
                
                # Ask if user wants to visualize
                if n > 1 and input("\nVisualize this sequence? (y/n): ").lower() == 'y':
                    PellGenerator.plot_sequence(sequence, f"First {n} Pell Numbers")
                
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '3':
            # Check if number is Pell
            try:
                num = get_positive_integer("Enter a number to check if it's a Pell number: ")
                if PellGenerator.is_pell_number(num):
                    print(f"\n{num} is a Pell number!")
                else:
                    print(f"\n{num} is NOT a Pell number.")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '4':
            # Performance comparison
            try:
                n = get_positive_integer("Enter the index to benchmark up to (max 30 for recursive): ")
                results = PellGenerator.benchmark(n)
                
                print("\nPerformance Comparison (in seconds):")
                print("-" * 40)
                for method, time_taken in results.items():
                    print(f"{method.capitalize():<12}: {time_taken:.6f}")
                
                # Show recommendation
                fastest = min(results, key=results.get)
                print(f"\nRecommendation: Use {fastest} method for best performance")
                
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '5':
            # Visualize sequence
            try:
                n = get_positive_integer("Enter the number of Pell numbers to visualize: ")
                if n < 2:
                    print("Please enter at least 2 to visualize a sequence.")
                    continue
                
                method = input("Choose method (recursive/memoization/iterative) [default: iterative]: ").lower() or 'iterative'
                sequence = generator.generate_sequence(n, method)
                PellGenerator.plot_sequence(sequence, f"First {n} Pell Numbers")
                
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '6':
            # Educational information
            print("\n" + "=" * 50)
            print("ABOUT PELL NUMBERS".center(50))
            print("=".center(50, "="))
            print("Pell numbers are an integer sequence similar to Fibonacci numbers,")
            print("but with a different recurrence relation:")
            print("\nP(0) = 0")
            print("P(1) = 1")
            print("P(n) = 2 * P(n-1) + P(n-2) for n > 1")
            print("\nThe sequence begins: 0, 1, 2, 5, 12, 29, 70, 169, 408, 985,...")
            print("\nPell numbers appear in approximations to the square root of 2,")
            print("in the definition of square triangular numbers, and in combinatorics.")
            print("=".center(50, "="))
            input("\nPress Enter to return to the main menu...")
        
        elif choice == '7':
            # Exit
            print("\nThank you for using the Pell Numbers Generator!")
            print("Exiting the program...")
            sys.exit(0)
        
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    # Clear the console for better presentation
    print("\n" * 100)
    
    # Welcome message
    print("=".center(50, "="))
    print("WELCOME TO THE PELL NUMBERS GENERATOR BY DAVID CALEB".center(70))
    print("=".center(50, "="))
    print("This program generates Pell numbers using different methods and provides")
    print("tools for analyzing and visualizing this mathematical sequence.")
    print("=".center(50, "="))
    input("\nPress Enter to continue to the main menu...")
    
    main()