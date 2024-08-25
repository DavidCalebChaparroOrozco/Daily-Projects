from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Initialize a list to hold the merged intervals
        merged_intervals = []
        i = 0
        n = len(intervals)
        
        # Add all intervals that end before the start of the newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            merged_intervals.append(intervals[i])
            i += 1
        
        # Merge all overlapping intervals with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        # Add the merged interval
        merged_intervals.append(newInterval)
        
        # Add all remaining intervals that start after the end of the newInterval
        while i < n:
            merged_intervals.append(intervals[i])
            i += 1
        
        return merged_intervals

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
intervals1 = [[1,3],[6,9]]
newInterval1 = [2,5]
print("Example 1:")
print("Input:", intervals1)
print("Output:", sol.insert(intervals1, newInterval1))
print("=".center(50,"="))

# Example 2
intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval2 = [4,8]
print("Example 2:")
print("Input:", intervals2)
print("Output:", sol.insert(intervals2, newInterval2))
print("=".center(50,"="))