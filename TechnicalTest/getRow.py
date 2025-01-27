class Solution:
    def getRow(self, rowIndex: int):
        # Initialize the first row with a single element 1
        row = [1]
        
        # Generate the specific row using dynamic programming approach
        for k in range(1, rowIndex + 1):
            # Create next row by calculating each element
            # Use the previous row's values to compute current row
            row.append(row[k-1] * (rowIndex - k + 1) // k)
        
        return row

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
rowIndex1 = 3
print("Example 1:")
print("Input:", rowIndex1)
print("Output:", sol.getRow(rowIndex1))
print("=".center(50,"="))

# Example 2
rowIndex2 = 0
print("Example 1:")
print("Input:", rowIndex2)
print("Output:", sol.getRow(rowIndex2))
print("=".center(50,"="))

# Example 3
rowIndex3 = 1
print("Example 1:")
print("Input:", rowIndex3)
print("Output:", sol.getRow(rowIndex3))
print("=".center(50,"="))