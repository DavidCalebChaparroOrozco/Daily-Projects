# Function to convert a number into its word representation
def number_to_words(num):
    # Define word representations for numbers 0-19
    units = ["zero", "one", "two", "three", "four", 
            "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", "fourteen", 
            "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    
    # Define word representations for tens (20, 30, ..., 90)
    tens = ["", "", "twenty", "thirty", "forty", 
            "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    # Handle numbers from 0 to 19
    if num < 20:
        return units[num]
    
    # Handle numbers from 20 to 99
    if num < 100:
        return tens[num // 10] + (" " + number_to_words(num % 10) if num % 10 != 0 else "")
    
    # Handle numbers from 100 to 999
    if num < 1000:
        return units[num // 100] + " hundred" + (" " + number_to_words(num % 100) if num % 100 != 0 else "")
    
    # Handle numbers from 1000 to 999999
    if num < 1000000:
        return number_to_words(num // 1000) + " thousand" + (" " + number_to_words(num % 1000) if num % 1000 != 0 else "")
    
    # Handle numbers from 1000000 to 999999999
    if num < 1000000000:
        return number_to_words(num // 1000000) + " million" + (" " + number_to_words(num % 1000000) if num % 1000000 != 0 else "")
    
    # Handle numbers greater than or equal to 1 billion
    return number_to_words(num // 1000000000) + " billion" + (" " + number_to_words(num % 1000000000) if num % 1000000000 != 0 else "")


# Example usage
if __name__ == "__main__":
    number = 123456789
    words = number_to_words(number)
    print(f"{number} in words is: {words}")