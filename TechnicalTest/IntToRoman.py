# IntToRoman
# Seven different symbols represent Roman numerals with the following values:
# Symbol	Value
# I	1
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1000

# Roman numerals are formed by appending the conversions of decimal place values from 
# highest to lowest. Converting a decimal place value into a Roman numeral has the 
# following rules:
#   If the value does not start with 4 or 9, select the symbol of the maximal value 
#       that can be subtracted from the input, append that symbol to the result, 
#       subtract its value, and convert the remainder to a Roman numeral.
#   If the value starts with 4 or 9 use the subtractive form representing one symbol 
#       subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): 
#       IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 
#       4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
#   Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent 
#       multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. 
#       If you need to append a symbol 4 times use the subtractive form.
# Given an integer, convert it to a Roman numeral.

class Solution(object):
    def intToRoman(self, num):
        # A list of tuples containing the decimal values and their corresponding Roman numeral symbols.
        roman_numerals = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        # Initialize an empty string to store the Roman numeral representation.
        result = ""
        
        # Iterate through the list of Roman numeral symbols.
        for value, symbol in roman_numerals:
            # Append the symbol to the result as long as the value is less than or equal to the input num.
            while num >= value:
                result += symbol
                num -= value

        # Return the Roman numeral representation of the input number.
        return result

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
num1 = 3749
print("Example 1:")
print("Input:", num1)
print("Example 1:", sol.intToRoman(num1))
print("=".center(50,"="))

# Example 2
num2 = 58
print("Example 2:")
print("Input:", num2)
print("Example 2:", sol.intToRoman(num2))  
print("=".center(50,"="))

# Example 3
num3 = 1994
print("Example 3:")
print("Input:", num3)
print("Example 3:", sol.intToRoman(num3))  
print("=".center(50,"="))