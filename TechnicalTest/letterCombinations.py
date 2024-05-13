# Given a string containing digits from 2-9 inclusive, return all possible letter 
# combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. 
# Note that 1 does not map to any letters.

class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        # Mapping digits to letters
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # Recursive function to generate combinations
        def backtrack(combination, next_digits):
            # Base case: if there are no digits left, add the current combination to the results list
            if not next_digits:
                result.append(combination)
            else:
                # Iterate over the letters corresponding to the next digit and make a recursive call
                for letter in digit_map[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        result = []
        backtrack('', digits)
        return result
    
# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
digits1 = "23"
print("Example 1:")
print("Input:", digits1)
print("Output:", sol.letterCombinations(digits1))
print("=".center(50,"="))

# Example 2
digits2 = ""
print("Example 2:")
print("Input:", digits2)
print("Output:", sol.letterCombinations(digits2))
print("=".center(50,"="))

# Example 3
digits3 = "2"
print("Example 2:")
print("Input:", digits3)
print("Output:", sol.letterCombinations(digits3))
print("=".center(50,"="))