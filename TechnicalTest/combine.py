class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        # Result list to store all the combinations
        result = []
        
        # Helper function to generate combinations using backtracking
        def backtrack(start, combination):
            # If the combination is of size k, add it to the result list
            if len(combination) == k:
                result.append(combination[:])  # Make a copy of the combination
                return
            
            # Iterate through the range from the current starting number to n
            for i in range(start, n + 1):
                # Add the current number to the combination
                combination.append(i)
                
                # Recursively call backtrack to generate further combinations
                backtrack(i + 1, combination)
                
                # Remove the last added number to backtrack and try another number
                combination.pop()
        
        # Start the backtracking process with the first number (1)
        backtrack(1, [])
        
        # Return the result list containing all combinations
        return result

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
n1 = 4
k1 = 2
print("Example 1:")
print("Input:", n1)
print("Output:",sol.combine(n1, k1))
print("=".center(50, "="))

# Example 2
n2 = 1
k2 = 1
print("Example 2:")
print("Input:", n2) 
print("Output:", sol.combine(n2, k2) )
print("=".center(50, "="))