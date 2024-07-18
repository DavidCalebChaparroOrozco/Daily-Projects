class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # Initialize result as an array of zeros
        result = [0] * (len(num1) + len(num2))

        # Reverse both numbers to make multiplication easier
        num1, num2 = num1[::-1], num2[::-1]

        # Multiply each digit of num1 with each digit of num2
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                result[i + j] += digit1 * digit2
                # Handle carry
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

        # Remove leading zeros and convert result back to string
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return ''.join(map(str, result[::-1]))

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
num1 = "2"
num2 = "3"
print("Example 1:")
print("Input num1:", num1,"Input num2:", num2)
print("Output:", sol.multiply(num1, num2))
print("=".center(50,"="))

# Example 2
num3 = "123"
num4 = "456"
print("Example 2:")
print("Input num3:", num3,"Input num4:", num4)
print("Output:", sol.multiply(num3, num4))
print("=".center(50,"="))