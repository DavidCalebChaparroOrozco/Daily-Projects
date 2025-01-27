class Solution:
    def generate(self, numRows: int):
        # Check if numRows is less than or equal to 0
        if numRows <= 0:
            return []
        
        # Initialize the result list with the first row
        result = [[1]]
        
        # Generate subsequent rows
        for i in range(1, numRows):
            # Create a new row starting with 1
            current_row = [1]
            
            # Calculate middle elements by summing adjacent elements from previous row
            for j in range(1, i):
                middle_value = result[i-1][j-1] + result[i-1][j]
                current_row.append(middle_value)
            
            # End the row with 1
            current_row.append(1)
            
            # Add the current row to the result
            result.append(current_row)
        
        return result

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
numRows1 = 5
print("Example 1:")
print("Input:", numRows1)
print("Output:", sol.generate(numRows1))
print("=".center(50,"="))

# Example 2
numRows2 = 1
print("Example 1:")
print("Input:", numRows2)
print("Output:", sol.generate(numRows2))
print("=".center(50,"="))