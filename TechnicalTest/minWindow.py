class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: If t is longer than s, no valid window exists
        if len(t) > len(s):
            return ""

        # Dictionary to keep track of the required character counts in t
        from collections import Counter
        required_chars = Counter(t)

        # Variables to track the minimum window substring
        left = 0
        right = 0
        min_left = 0
        min_size = float("inf")
        chars_needed = len(t)

        # Iterate over the string s using the right pointer
        while right < len(s):
            # If the current character is in t, decrement chars_needed
            if required_chars[s[right]] > 0:
                chars_needed -= 1
            required_chars[s[right]] -= 1
            right += 1

            # Once we have a valid window, try to minimize it
            while chars_needed == 0:
                # Update the minimum window if a smaller one is found
                if right - left < min_size:
                    min_left = left
                    min_size = right - left

                # Move the left pointer to shrink the window
                required_chars[s[left]] += 1
                if required_chars[s[left]] > 0:
                    chars_needed += 1
                left += 1

        # If no valid window is found, return an empty string
        return s[min_left:min_left + min_size] if min_size != float("inf") else ""

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
s1 = "ADOBECODEBANC"
t1 = "ABC"
print("Example 1:")
print("Input:", s1)
print("Output:",sol.minWindow(s1, t1))
print("=".center(50, "="))

# Example 2
s2 = "a"
t2 = "a"
print("Example 2:")
print("Input:", s2) 
print("Output:", sol.minWindow(s2, t2) )
print("=".center(50, "="))

# Example 3
s3 = "a"
t3 = "aa"
print('Example 3:')
print("Input:", s3)
print("Output:", sol.minWindow(s3, t3)  )
print("=".center(50, "="))
