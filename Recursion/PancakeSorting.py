"""
Pancake Sorting Algorithm Implementation
This program demonstrates the Pancake Sort algorithm, which sorts an array by repeatedly flipping
portions of the array. The implementation includes both recursive sorting and an interactive
menu system for demonstration purposes.

Author: David Caleb
"""

# Import necessary libraries
import random
from typing import List

# A class that implements the Pancake Sort algorithm with various utility methods.
class PancakeSorter:
    """    
    Attributes:
        current_array: The array currently being sorted or manipulated.
    """
    
    # Initialize the PancakeSorter with an empty array.
    def __init__(self):
        self.current_array: List[int] = []
    
    # Reverse the order of the first k elements in the array.
    @staticmethod
    def flip(arr: List[int], k: int):
        """    
        Args:
            arr: The array to be modified
            k: Number of elements to flip (1-based index)
        """
        if k < 2:
            return
        left, right = 0, k - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    # Find the index of the maximum element in the first n elements of the array.
    @staticmethod
    def find_max_index(arr: List[int], n: int) -> int:
        """        
        Args:
            arr: The array to search
            n: Number of elements to consider
            
        Returns:
            Index of the maximum element
        """
        max_idx = 0
        for i in range(1, n):
            if arr[i] > arr[max_idx]:
                max_idx = i
        return max_idx

    # Recursively sort the array with step-by-step printing of flip operations.
    def sort_with_prints(self, arr: List[int], n: int):
        """    
        Args:
            arr: The array to be sorted
            n: Number of elements to sort (shrinks with each recursion)
        """
        if n == 1:
            return
        
        max_idx = self.find_max_index(arr, n)
        
        if max_idx != n - 1:
            if max_idx != 0:
                self.flip(arr, max_idx + 1)
                print(f"Flip {max_idx + 1}: {arr}")
            
            self.flip(arr, n)
            print(f"Flip {n}: {arr}")
        
        self.sort_with_prints(arr, n - 1)

    # Recursively sort the array without printing intermediate steps.
    def silent_sort(self, arr: List[int], n: int):
        """    
        Args:
            arr: The array to be sorted
            n: Number of elements to sort (shrinks with each recursion)
        """
        if n == 1:
            return
        
        max_idx = self.find_max_index(arr, n)
        
        if max_idx != n - 1:
            if max_idx != 0:
                self.flip(arr, max_idx + 1)
            self.flip(arr, n)
        
        self.silent_sort(arr, n - 1)

    # Perform pancake sort on the given array with optional verbosity.
    def pancake_sort(self, arr: List[int], verbose: bool = True) -> List[int]:
        """    
        Args:
            arr: The array to be sorted
            verbose: Whether to print sorting process
            
        Returns:
            The sorted array
        """
        if verbose:
            print(f"Original array: {arr}")
            self.sort_with_prints(arr, len(arr))
        else:
            self.silent_sort(arr, len(arr))
        return arr


# Interactive menu system for demonstrating the Pancake Sort algorithm.
class PancakeSortMenu:
    """    
    Attributes:
        sorter (PancakeSorter): An instance of the PancakeSorter class
    """
    
    # Initialize the menu with a PancakeSorter instance.
    def __init__(self):
        self.sorter = PancakeSorter()
    
    @staticmethod
    def display_menu():
        print("\nPancake Sorting Algorithm by David Caleb")
        print("Please choose an option:")
        print("1. Enter a new array to sort")
        print("2. Sort current array with step-by-step visualization")
        print("3. Sort current array with final result only")
        print("4. Generate random array example")
        print("5. View current array")
        print("6. Exit")

    def app(self):
        while True:
            self.display_menu()
            choice = input("Please enter your choice (1-6): ")
            
            if choice == "1":
                self.handle_new_array()
            elif choice == "2":
                self.sort_with_visualization()
            elif choice == "3":
                self.sort_without_visualization()
            elif choice == "4":
                self.generate_random_array()
            elif choice == "5":
                self.view_current_array()
            elif choice == "6":
                print("Exiting Pancake Sorting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1-6.")

    # Handle user input for a new array to sort.
    def handle_new_array(self):
        print("\nEnter numbers separated by spaces (e.g., '3 1 4 2'):")
        try:
            user_input = input("> ")
            self.sorter.current_array = [int(num) for num in user_input.split()]
            print(f"New array set: {self.sorter.current_array}")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    # Sort the current array with step-by-step visualization.
    def sort_with_visualization(self):
        if not self.sorter.current_array:
            print("No array to sort. Please enter or generate an array first.")
            return
        
        print("\nSorting process with step-by-step visualization:")
        arr_copy = self.sorter.current_array.copy()
        self.sorter.pancake_sort(arr_copy)

    # Sort the current array and only show the final result.
    def sort_without_visualization(self):
        if not self.sorter.current_array:
            print("No array to sort. Please enter or generate an array first.")
            return
        
        print("\nSorting current array...")
        arr_copy = self.sorter.current_array.copy()
        self.sorter.pancake_sort(arr_copy, verbose=False)
        print(f"Original array: {self.sorter.current_array}")
        print(f"Sorted array: {arr_copy}")
        self.sorter.current_array = arr_copy

    # Generate a random array for demonstration purposes.
    def generate_random_array(self):
        size = random.randint(5, 10)
        self.sorter.current_array = [random.randint(1, 100) for _ in range(size)]
        print(f"Generated random array: {self.sorter.current_array}")

    # Display the current array being worked on.
    def view_current_array(self):
        if self.sorter.current_array:
            print(f"\nCurrent array: {self.sorter.current_array}")
        else:
            print("No array currently loaded. Please enter or generate one.")


def main():
    print("Pancake Sorting Algorithm Implementation")
    print("=".center(50, "="))
    
    # Demonstrate the algorithm with a sample array
    sorter = PancakeSorter()
    sample_array = [3, 1, 4, 2, 6, 5]
    print("\nDemonstration with sample array:")
    print(f"Original array: {sample_array}")
    sorted_array = sorter.pancake_sort(sample_array.copy())
    print(f"Final sorted array: {sorted_array}")
    
    # Start interactive menu
    menu = PancakeSortMenu()
    menu.app()


if __name__ == "__main__":
    main()