from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # This function handles the process of fully justifying the text.
        
        result = []  # List to store the final lines of justified text
        current_line = []  # List to store words for the current line
        current_length = 0  # Tracks the total length of words in the current line
        
        for word in words:
            # Check if adding the current word would exceed maxWidth (considering spaces between words)
            if current_length + len(word) + len(current_line) > maxWidth:
                # Distribute spaces evenly between words in the current line
                for i in range(maxWidth - current_length):
                    # Distribute extra spaces more to the left slots
                    current_line[i % (len(current_line) - 1 or 1)] += ' '
                
                # Join the words with spaces and add the line to the result
                result.append(''.join(current_line))
                # Reset current_line and current_length for the next line
                current_line, current_length = [], 0
            
            # Add the current word to the line and update the current length
            current_line.append(word)
            current_length += len(word)
        
        # Handling the last line: left-justified with remaining spaces at the end
        result.append(' '.join(current_line).ljust(maxWidth))
        
        return result
    
# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
words1 = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth1 = 16
print("Example 1:")
print("Input:", words1)
print("Output:", sol.fullJustify(words1,maxWidth1))
print("=".center(50,"="))

# Example 2
print("=".center(50,"="))
words2 = ["What","must","be","acknowledgment","shall","be"]
maxWidth2 = 16
print("Example 1:")
print("Input:", words2)
print("Output:", sol.fullJustify(words2,maxWidth2))
print("=".center(50,"="))