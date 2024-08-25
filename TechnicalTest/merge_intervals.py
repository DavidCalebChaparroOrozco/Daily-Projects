from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # If the intervals list is empty, return an empty list
        if not intervals:
            return []
        
        # Sort the intervals by their starting times
        intervals.sort(key=lambda x: x[0])
        
        # Initialize a list to hold the merged intervals
        merged_intervals = []
        
        # Start with the first interval
        current_interval = intervals[0]
        
        # Iterate through the sorted intervals
        for next_interval in intervals[1:]:
            # If the current interval overlaps with the next interval, merge them
            if current_interval[1] >= next_interval[0]:
                current_interval[1] = max(current_interval[1], next_interval[1])
            else:
                # If they don't overlap, add the current interval to the merged list
                merged_intervals.append(current_interval)
                # Move on to the next interval
                current_interval = next_interval
        
        # Don't forget to add the last interval
        merged_intervals.append(current_interval)
        
        return merged_intervals

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
intervals1 = [[1,3],[2,6],[8,10],[15,18]]
print("Example 1:")
print("Input:", intervals1)
print("Output:", sol.merge(intervals1))
print("=".center(50,"="))

# Example 2
intervals2 = [[1,4],[4,5]]
print("Example 2:")
print("Input:", intervals2)
print("Output:", sol.merge(intervals2))
print("=".center(50,"="))