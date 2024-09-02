# Determine if the given list can be partitioned into two subsets with equal sum.
def can_partition(nums):
    """
    Args:
        nums: List of integers.
    Returns:
        bool: True if the list can be partitioned into two subsets with equal sum, otherwise False.
    """
    total_sum = sum(nums)
    
    # If the total sum is odd, we can't partition it into two equal subsets
    if total_sum % 2 != 0:
        return False
    
    # We aim to find a subset with sum equal to half of total_sum
    target_sum = total_sum // 2
    
    subset = []
    if can_partition_recursive(nums, target_sum, len(nums) - 1, subset):
        print(f"The subset with sum {target_sum} is: {subset}")
        remaining_subset = [num for num in nums if num not in subset or subset.remove(num)]
        print(f"The remaining subset is: {remaining_subset}")
        return True
    else:
        return False

# Helper function to determine if a subset with the given target_sum exists using recursion.
def can_partition_recursive(nums, target_sum, index, subset):
    """    
    Args:
        nums: List of integers.
        target_sum: The target sum we want to find in the subset.
        index: The current index in the list.
        subset: List to store the current subset.
    Returns:
        bool: True if a subset with the target sum exists, otherwise False.
    """
    # Base case: if target_sum is 0, we found a valid subset
    if target_sum == 0:
        return True
    
    # Base case: if no more items left or target_sum becomes negative
    if index < 0 or target_sum < 0:
        return False
    
    # Option 1: Exclude the current number and move to the next
    if can_partition_recursive(nums, target_sum, index - 1, subset):
        return True
    
    # Option 2: Include the current number and reduce the target_sum
    subset.append(nums[index])
    if can_partition_recursive(nums, target_sum - nums[index], index - 1, subset):
        return True
    
    # Backtrack: Remove the last number added if it doesn't lead to a solution
    subset.pop()
    
    return False

# Example usage
nums = [1, 5, 11, 5]
if can_partition(nums):
    print("The list can be partitioned into two subsets with equal sum.")
else:
    print("The list cannot be partitioned into two subsets with equal sum.")