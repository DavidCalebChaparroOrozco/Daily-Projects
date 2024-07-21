# Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
# that the number could represent. A mapping of digit to letters (just like on the telephone buttons) 
# is given below. Note that 1 does not map to any letters.

def letter_combinations(digits):
    """
    digits: A string containing the digits
    return: A list of all possible letter combinations
    """
    
    # Dictionary to map digits to their corresponding letters
    phone_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    
# Helper function to perform backtracking to find all possible combinations.
    def backtrack(combination, next_digits):
        """
        combination: Current combination of letters
        next_digits: Remaining digits to process
        """
        # If there are no more digits to check, add the combination to the result
        if len(next_digits) == 0:
            combinations.append(combination)
        # If there are still digits to check
        else:
            # Iterate over all letters which map to the next available digit
            for letter in phone_map[next_digits[0]]:
                # Append the current letter to the combination and proceed with the next digit
                backtrack(combination + letter, next_digits[1:])
    
    # List to store the combinations
    combinations = []
    
    if digits:
        backtrack("", digits)
    
    return combinations

# Example usage
phone_number = "23"
print("Possible letter combinations for phone number", phone_number, "are:")
print(letter_combinations(phone_number))
