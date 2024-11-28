from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # List to store valid IP addresses
        res = []
        
        # Helper function to perform backtracking
        def backtrack(start: int, dots: int, current_ip: str):
            # If we have placed 4 dots and used all characters in the string
            if dots == 4 and start == len(s):
                res.append(current_ip[:-1])  # Append the valid IP without the trailing dot
                return
            
            # If we have placed more than 4 dots or used all characters without forming a valid IP
            if dots > 4 or start >= len(s):
                return
            
            # Try to form a segment by choosing 1 to 3 digits
            for j in range(start, min(start + 3, len(s))):
                segment = s[start:j + 1]
                
                # Check if the segment is valid
                if (len(segment) > 1 and segment[0] == "0") or int(segment) > 255:
                    continue
                
                # Recursive call to place the next dot
                backtrack(j + 1, dots + 1, current_ip + segment + ".")
        
        # Start backtracking from index 0 with 0 dots placed and an empty current IP string
        backtrack(0, 0, "")
        
        return res

# Example usage
sol = Solution()

# Example 1
print("=".center(50, "="))
print("Example 1:")
input_str1 = "25525511135"
output1 = sol.restoreIpAddresses(input_str1)
print("Input:", input_str1)
print("Output:", output1)
print("=".center(50, "="))

# Example 2
print("Example 2:")
input_str2 = "0000"
output2 = sol.restoreIpAddresses(input_str2)
print("Input:", input_str2)
print("Output:", output2)
print("=".center(50, "="))

# Example 3
print("Example 3:")
input_str3 = "101023"
output3 = sol.restoreIpAddresses(input_str3)
print("Input:", input_str3)
print("Output:", output3)
print("=".center(50, "="))