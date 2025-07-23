class Solution:
    # Split the versions into lists of revision strings
    def compareVersion(self, version1: str, version2: str) -> int:
        revisions1 = version1.split('.')
        revisions2 = version2.split('.')
        
        # Get the maximum number of revisions between the two versions
        max_length = max(len(revisions1), len(revisions2))
        
        for i in range(max_length):
            # Get the current revision for each version, default to 0 if out of bounds
            rev1 = int(revisions1[i]) if i < len(revisions1) else 0
            rev2 = int(revisions2[i]) if i < len(revisions2) else 0
            
            # Compare the revisions
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
        
        # If all revisions are equal
        return 0
    
# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
version1 = "1.2"
version2 = "1.10"
print("Example 1:")
print("Input:", version1, " and ", version2)
print("Output:", sol.compareVersion(version1, version2))

# Example 2
print("=".center(50, "="))
version01 = "1.01"
version02 = "1.001"
print("Example 2:")
print("Input:", version01, " and ", version02)
print("Output:", sol.compareVersion(version01, version02))
print("=".center(50, "="))

# Example 3
version001 = "1.0"
version002 = "1.0.0.0"
print("Example 3:")
print("Input:", version001, " and ", version002)
print("Output:", sol.compareVersion(version001, version002))
print("=".center(50, "="))