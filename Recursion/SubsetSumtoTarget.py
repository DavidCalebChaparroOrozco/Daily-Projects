# This function finds all subsets of 'nums' that sum up to 'target'.
def find_subsets(nums, target):
    """    
    nums: List of integers
    target: Target sum
    return: List of lists containing all subsets that sum to the target
    """
    result = []
    
    # A helper function that performs backtracking to find all combinations.
    def backtrack(start, path, current_sum):
        """    
        start: The starting index for the current recursive call
        path: The current subset being built
        current_sum: The current sum of the subset
        """
        # If the current sum matches the target, add the path to the result
        if current_sum == target:
            result.append(path.copy())
            return
        
        # If the current sum exceeds the target, no need to continue
        if current_sum > target:
            return
        
        # Explore further elements in nums
        for i in range(start, len(nums)):
            # Include nums[i] in the subset and explore further
            path.append(nums[i])
            backtrack(i + 1, path, current_sum + nums[i])  # Move to next index
            path.pop()  # Backtrack: remove the last element added
    
    # Start backtracking from index 0 with an empty path and a sum of 0
    backtrack(0, [], 0)
    
    return result

# Example usage:
if __name__ == "__main__":
    numbers = [2, 3, 5, 6, 7]
    target_sum = 10
    subsets = find_subsets(numbers, target_sum)
    
    print("Subsets that sum to", target_sum, "are:", subsets)