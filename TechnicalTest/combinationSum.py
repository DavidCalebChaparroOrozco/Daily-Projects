from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Helper function to perform backtracking
        def backtrack(remaining_target: int, combination: List[int], start: int):
            # If the remaining target is 0, we found a valid combination
            if remaining_target == 0:
                result.append(list(combination))
                return
            
            # Loop through the candidates starting from 'start' index
            for i in range(start, len(candidates)):
                # If the candidate exceeds the remaining target, skip it
                if candidates[i] > remaining_target:
                    continue
                
                # Include the candidate in the current combination
                combination.append(candidates[i])
                
                # Recursively call backtrack with updated remaining target
                backtrack(remaining_target - candidates[i], combination, i)
                
                # Remove the last candidate added to backtrack
                combination.pop()
        
        # Initialize the result list
        result = []
        
        # Start the backtracking process
        backtrack(target, [], 0)
        
        return result

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
candidates1 = [2,3,6,7]
target1 = 7
print("Example 1:")
print("Input:", candidates1)
print("Output:", sol.combinationSum(candidates1, target1))
print("=".center(50,"="))

# Example 2
candidates2 = [2, 3, 5]
target2 = 8
print("Example 2:")
print("Input:", candidates2)
print("Output:", sol.combinationSum(candidates2, target2))
print("=".center(50,"="))

# Example 3
candidates3 = [2]
target3 = 1
print("Example 2:")
print("Input:", candidates3)
print("Output:", sol.combinationSum(candidates3, target3))
print("=".center(50,"="))