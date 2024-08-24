# Gray Code Generator: Generates n-bit Gray code using recursion.

# Importing necessary libraries
import math as mt

# This function generates all n-bit Gray codes and prints the generated codes.
def generateGrayarr(n):
    """
    n: An integer representing the number of bits for the Gray code
    return: None (The function prints the Gray codes)
    """
    
    # Base case: If n is 0 or negative, there are no Gray codes to generate.
    if n <= 0:
        return

    # 'arr' will store all generated Gray codes.
    arr = list()

    # Start with the initial one-bit patterns: "0" and "1".
    arr.append("0")
    arr.append("1")

    # Variable 'i' will control the number of Gray codes generated in each iteration.
    i = 2

    # This loop generates 2*i Gray codes from the previously generated i codes until all n-bit codes are generated.
    while True:
        # If the number of generated codes equals or exceeds 2^n, stop the generation process.
        if i >= 1 << n:
            break

        # Append the previously generated codes in reverse order to the array.
        # This effectively doubles the number of codes in 'arr'.
        for j in range(i - 1, -1, -1):
            arr.append(arr[j])

        # Prefix '0' to the first half of the current Gray codes.
        for j in range(i):
            arr[j] = "0" + arr[j]

        # Prefix '1' to the second half of the current Gray codes.
        for j in range(i, 2 * i):
            arr[j] = "1" + arr[j]

        # Double the number of Gray codes in the next iteration.
        i = i << 1

    # Print all the generated n-bit Gray codes.
    for i in range(len(arr)):
        print(arr[i])

# Driver Code to test the function with 3-bit Gray codes
print("Example:")
print("Input:", 5)
print("Output:")
generateGrayarr(5)
print("=".center(50,"="))