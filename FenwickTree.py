# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Union

# An enhanced Fenwick Tree (Binary Indexed Tree) implementation with visualization capabilities.
# The Fenwick Tree is a data structure that efficiently maintains prefix sums
# and supports point updates in logarithmic time.
class FenwickTree:    
    # Initialize the Fenwick Tree.
    def __init__(self, size: int, values: List[Union[int, float]] = None):
        self.size = size
        # 1-based indexing with extra buffer
        self.tree = [0] * (self.size + 2)  
        
        # Store original values for visualization
        if values is not None and len(values) == size:
            # 1-based indexing
            self.data = [0] + values.copy()  
            self._build_tree()
        else:
            self.data = [0] * (self.size + 1)  # 1-based indexing
    
    # Build the Fenwick Tree from the initial values in O(n) time.
    def _build_tree(self) -> None:
        # Create prefix sum array
        prefix = [0] * (self.size + 1)
        for i in range(1, self.size + 1):
            prefix[i] = prefix[i - 1] + self.data[i]
        
        # Build the tree using prefix sums
        for i in range(1, self.size + 1):
            self.tree[i] = prefix[i] - prefix[i - self._lsb(i)]
    
    # Get the least significant bit of a number.
    def _lsb(self, num: int) -> int:
        return num & -num
    
    # Update the value at a specific index by adding a delta.
    def update(self, index: int, delta: Union[int, float]) -> None:
        if index < 1 or index > self.size:
            raise IndexError("Index out of bounds")
            
        self.data[index] += delta
        while index <= self.size:
            self.tree[index] += delta
            # Move to parent node
            index += self._lsb(index)  
    
    # Query the prefix sum from index 1 to the given index.
    def query(self, index: int) -> Union[int, float]:
        if index < 1 or index > self.size:
            raise IndexError("Index out of bounds")
            
        res = 0
        while index > 0:
            res += self.tree[index]
            # Move to parent node
            index -= self._lsb(index)  
        return res
    
    # Query the sum of elements in the range [left, right].
    def range_query(self, left: int, right: int) -> Union[int, float]:
        return self.query(right) - self.query(left - 1)
    
    # Visualize the Fenwick Tree structure using matplotlib.
    def visualize(self) -> None:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Visualize the original data
        ax1.bar(range(1, self.size + 1), self.data[1:], color='skyblue')
        ax1.set_title('Original Data')
        ax1.set_xlabel('Index (1-based)')
        ax1.set_ylabel('Value')
        ax1.set_xticks(range(1, self.size + 1))
        
        # Visualize the tree structure
        tree_display = self.tree[1:self.size + 1]
        ax2.bar(range(1, self.size + 1), tree_display, color='lightgreen')
        
        # Annotate each bar with its coverage
        for i in range(1, self.size + 1):
            coverage = []
            j = i
            while j <= self.size:
                coverage.append(str(j))
                j += self._lsb(j)
            ax2.text(i, tree_display[i-1] + 0.1, 
                    f'Covers: {", ".join(coverage)}', 
                    ha='center', va='bottom', rotation=90, fontsize=8)
        
        ax2.set_title('Fenwick Tree Structure')
        ax2.set_xlabel('Node Index')
        ax2.set_ylabel('Cumulative Value')
        ax2.set_xticks(range(1, self.size + 1))
        
        plt.tight_layout()
        plt.show()
    
    def __repr__(self) -> str:
        """String representation of the Fenwick Tree."""
        return (f"FenwickTree(size={self.size})\n"
                f"Original Data: {self.data[1:]}\n"
                f"Tree Structure: {self.tree[1:self.size + 1]}")


# Example Usage with Visualization
if __name__ == "__main__":
    print("Fenwick Tree Demonstration by David Caleb")

    # Sample data
    data = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2]
    print(f"Original data: {data}")
    
    # Initialize Fenwick Tree
    ft = FenwickTree(len(data), data)
    print("\nInitialized Fenwick Tree:")
    print(ft)
    
    # Perform some queries
    print("\nQuery Results:")
    print(f"Prefix sum up to index 5: {ft.query(5)}")
    print(f"Range sum from index 3 to 7: {ft.range_query(3, 7)}")
    
    # Perform an update
    print("\nUpdating index 4 by +2...")
    ft.update(4, 2)
    print(f"New prefix sum up to index 5: {ft.query(5)}")
    
    # Visualize the tree
    print("\nVisualizing the Fenwick Tree structure...")
    ft.visualize()