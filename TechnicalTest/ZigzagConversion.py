# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);

class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create an empty list for each row
        rows = [''] * numRows
        
        # Initialize variables for direction and current row
        direction = 1  # 1 for down, -1 for up
        row = 0
        
        # Iterate through the string, placing each character in the appropriate row
        for char in s:
            rows[row] += char
            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1
            row += direction
        
        # Concatenate all rows to form the final converted string
        return ''.join(rows)
    
# Create an instance of the Solution class
sol = Solution()

# Define an input string and the number of rows
s1 = "PAYPALISHIRING"
numRows = 3

# Call the convert function and display the result in the output
print(sol.convert(s1, numRows))
print("=".center(50,"="))

# Define an input string and the number of rows
s2 = "PAYPALISHIRING"
numRows = 4

# Call the convert function and display the result in the output
print(sol.convert(s2, numRows))
print("=".center(50,"="))


# Define an input string and the number of rows
s3 = "A"
numRows = 1

# Call the convert function and display the result in the output
print(sol.convert(s3, numRows))
print("=".center(50,"="))