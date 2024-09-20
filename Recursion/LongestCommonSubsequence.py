# Function to find the Longest Common Subsequence (LCS) of two strings using recursion
def lcs_recursive(X, Y):
    """
    Calculate the length of the Longest Common Subsequence (LCS) between two strings
    using a recursive approach.
    
    Args:
    X: First string
    Y: Second string
    
    Returns:
    int: Length of the LCS
    """
    
    # Helper function to perform the recursive LCS calculation
    def lcs_helper(m, n):
        # Base case: If either string is empty, the LCS length is 0
        if m == 0 or n == 0:
            return 0

        # If the last characters of both strings match, move diagonally and add 1 to the result
        if X[m - 1] == Y[n - 1]:
            return 1 + lcs_helper(m - 1, n - 1)
        
        # If the last characters do not match, find the maximum LCS length by ignoring
        # the last character of either string and taking the larger result
        else:
            return max(lcs_helper(m, n - 1), lcs_helper(m - 1, n))

    # Lengths of the input strings
    m = len(X)
    n = len(Y)
    
    # Call the helper function to compute LCS length
    return lcs_helper(m, n)

# Driver code to test the recursive LCS function
if __name__ == "__main__":
    # Example strings
    X = "AGGTAB"
    Y = "GXTXAYB"
    
    # Calling the recursive LCS function and printing the result
    lcs_length = lcs_recursive(X, Y)
    print("Length of Longest Common Subsequence is", lcs_length)