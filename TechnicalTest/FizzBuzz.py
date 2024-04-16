# FizzBuzz

# Write a program that prints the numbers from 1 to n, where n is a given number, but with the following conditions:
# If the number is divisible by 3, print "Fizz" instead of the number.
# If the number is divisible by 5, print "Buzz" instead of the number.
# If the number is divisible by both 3 and 5, print "FizzBuzz" instead of the number.
# For numbers that do not meet any of these conditions, print the number as it is.
# The goal is to write an efficient program that implements these rules.

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Initialize an empty list to store the FizzBuzz sequence
        result = []
        # Iterate from 1 to n (inclusive)
        for i in range(1, n+1):
            # Check if the current number is divisible by both 3 and 5
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            # Check if the current number is divisible by 3
            elif i % 3 == 0:
                result.append("Fizz")
            # Check if the current number is divisible by 5
            elif i % 5 == 0:
                result.append("Buzz")
            # If none of the above conditions are met, append the number as string
            else:
                result.append(str(i))
        # Return the FizzBuzz sequence
        return result