from itertools import permutations

# Load words from a text file into a set for quick lookup.
def load_dictionary(file_path):
    """    
    file_path: Path to the dictionary file (each line should have one word).
    return: A set containing all words in the dictionary.
    """
    with open(file_path, 'r') as file:
        words = {line.strip().lower() for line in file}
    return words

# Find all valid anagrams for a given set of letters based on a provided dictionary.
def find_anagrams(letters, dictionary):
    """    
    letters: A string of letters for which to find anagrams.
    dictionary: A set of valid words.
    return: A set of valid anagrams found in the dictionary.
    """
    # Generate all permutations of the given letters
    permuted_words = {''.join(p) for p in permutations(letters)}
    
    # Check which permutations are valid words in the dictionary
    valid_anagrams = {word for word in permuted_words if word in dictionary}
    
    return valid_anagrams

def main():
    # Path to the dictionary file - you can replace this with your own path
    dictionary_file = 'dictionary.txt'
    
    # Load the dictionary into a set
    dictionary = load_dictionary(dictionary_file)
    
    # Input letters for which to find anagrams
    letters = input("Enter a set of letters: ").strip().lower()
    
    # Find valid anagrams
    anagrams = find_anagrams(letters, dictionary)
    
    # Display the results
    if anagrams:
        print(f"Valid anagrams found: {', '.join(anagrams)}")
    else:
        print("No valid anagrams found.")

if __name__ == "__main__":
    main()