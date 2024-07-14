# Given a collection of candidate numbers (candidates) and a target number (target), 
# find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Define the backtracking function
        def backtrack(start, target, path):
            # If the target is zero, add the current path to the result
            if target == 0:
                result.append(path)
                return
            # If the target is less than zero, stop further exploration
            if target < 0:
                return
            # Iterate through the candidates starting from the given index
            for i in range(start, len(candidates)):
                # Skip duplicate candidates to avoid redundant combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # Recursively explore further with the next index and updated target and path
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        # Sort the candidates to handle duplicates and for easier processing
        candidates.sort()
        # Initialize the result list
        result = []
        # Start the backtracking process from index 0 with an empty path
        backtrack(0, target, [])
        # Return the final result containing all unique combinations
        return result


# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
candidates1 = [10,1,2,7,6,1,5]
target1 = 8
print("Example 1:")
print("Input:", candidates1)
print("Output:", sol.combinationSum2(candidates1, target1))
print("=".center(50,"="))

# Example 2
candidates2 = [2,5,2,1,2]
target2 = 5
print("Example 2:")
print("Input:", candidates2)
print("Output:", sol.combinationSum2(candidates2, target2))
print("=".center(50,"="))