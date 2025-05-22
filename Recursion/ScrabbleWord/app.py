# Import necessary libraries
import json
import os
import sys
from collections import defaultdict
from typing import List, Dict, Set, Optional

# Constants
DICTIONARY_FILE_EN = 'dictionary_en.json'
DICTIONARY_FILE_ES = 'dictionary_es.json'
SCORES = {
    'en': {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
        'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3,
        'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
        'y': 4, 'z': 10
    },
    'es': {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
        'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'ñ': 8, 'o': 1,
        'p': 3, 'q': 5, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 8,
        'x': 8, 'y': 4, 'z': 10
    }
}
# Character to represent blank tiles/wildcards
WILDCARD_CHAR = '?'  


# Handles dictionary loading and word validation.
class Dictionary:
    
    def __init__(self, language: str = 'en'):
        self.language = language
        self.words = set()
        self.word_tree = {}
        self.load_dictionary()
    
    # Load the appropriate dictionary file based on language.
    def load_dictionary(self) -> None:
        try:
            filename = DICTIONARY_FILE_EN if self.language == 'en' else DICTIONARY_FILE_ES
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.words = set(data['words'])
                self.word_tree = data['word_tree']
            print(f"Dictionary loaded successfully ({len(self.words)} words)")
        except FileNotFoundError:
            print(f"Error: Dictionary file not found for language '{self.language}'")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error: Invalid dictionary file format for language '{self.language}'")
            sys.exit(1)
    
    # Check if a word exists in the dictionary.
    def is_valid_word(self, word: str) -> bool:
        return word.lower() in self.words


# Core word finding logic with recursive search and pruning.
class WordFinder:
    
    def __init__(self, dictionary: Dictionary):
        self.dictionary = dictionary
        self.results = set()
    
    # Find all valid words that can be formed from the given letters.
    def find_words(self, letters: str, min_length: int = 2, max_length: Optional[int] = None) -> Set[str]:
        """    
        Args:
            letters: Available letters (can include wildcards)
            min_length: Minimum word length to consider
            max_length: Maximum word length to consider (None for no limit)
        
        Returns:
            Set of valid words sorted by length (then alphabetically)
        """
        if max_length is None:
            max_length = len(letters)
        
        self.results = set()
        letter_counts = self._count_letters(letters.lower())
        self._search_words(letter_counts, [], self.dictionary.word_tree, min_length, max_length)
        
        # Sort results by length (descending), then alphabetically
        return sorted(self.results, key=lambda x: (-len(x), x))
    
    # Count the occurrences of each letter (excluding wildcards).
    def _count_letters(self, letters: str) -> Dict[str, int]:
        counts = defaultdict(int)
        for char in letters:
            if char != WILDCARD_CHAR:
                counts[char] += 1
        return counts
    
    # Recursive function to search for valid words with pruning.
    def _search_words( self, letter_counts: Dict[str, int], current_path: List[str], 
                    current_node: Dict, min_length: int, max_length: int, 
                    wildcards_used: int = 0, total_wildcards: Optional[int] = None) -> None:
        """
        Args:
            letter_counts: Remaining letters available
            current_path: Current path in the word tree
            current_node: Current node in the word tree
            min_length: Minimum word length
            max_length: Maximum word length
            wildcards_used: Number of wildcards used in current path
            total_wildcards: Total wildcards available (None for unlimited)
        """
        # Base case: if current path forms a valid word, add to results
        if '#' in current_node and min_length <= len(current_path) <= max_length:
            self.results.add(''.join(current_path))
        
        # Recursive case: explore all possible next letters
        for char, node in current_node.items():
            if char == '#':
                continue  # Skip the word termination marker
            
            # Check if we can use this letter (either from available letters or wildcard)
            if letter_counts.get(char, 0) > 0:
                # Use the actual letter
                letter_counts[char] -= 1
                current_path.append(char)
                self._search_words(letter_counts, current_path, node, min_length, max_length, wildcards_used, total_wildcards)
                current_path.pop()
                letter_counts[char] += 1
            elif (total_wildcards is None or wildcards_used < total_wildcards) and char != WILDCARD_CHAR:
                # Use a wildcard to represent this letter
                current_path.append(char)
                self._search_words(letter_counts, current_path, node, min_length, max_length, wildcards_used + 1, total_wildcards)
                current_path.pop()


# Provides Scrabble-specific functionality.
class ScrabbleHelper:
    
    # Calculate the Scrabble score for a word.
    @staticmethod
    def calculate_word_score(word: str, language: str = 'en') -> int:
        score = 0
        for letter in word.lower():
            score += SCORES[language].get(letter, 0)
        return score
    
    # Display words with their Scrabble scores.
    @staticmethod
    def display_word_scores(words: List[str], language: str = 'en') -> None:
        if not words:
            print("No words found.")
            return
        
        max_word_length = max(len(word) for word in words)
        print("\nFound Words:")
        print("-" * (max_word_length + 10))
        for word in words:
            score = ScrabbleHelper.calculate_word_score(word, language)
            print(f"{word:<{max_word_length}} - {score} points")
        print("-" * (max_word_length + 10))
        print(f"Total words found: {len(words)}")

# Handles user interaction and menu system.
class UserInterface:
    
    def __init__(self):
        self.language = 'en'
        self.dictionary = Dictionary(self.language)
        self.word_finder = WordFinder(self.dictionary)
        self.letters = ''
    
    # Clear the console screen
    def clear_screen(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
    
    # Display the application header
    def display_header(self) -> None:
        self.clear_screen()
        print("=".center(50, "="))
        print("SCRABBLE WORD FINDER".center(50))
        print("=".center(50, "="))
        print(f"Language: {self.language.upper()} | Letters: {self.letters or 'None'}")
        print("-".center(50, "-"))
    
    # Display the main menu and handle user input.
    def main_menu(self) -> None:
        while True:
            self.display_header()
            print("MAIN MENU:")
            print("1. Enter your letters")
            print("2. Change language (current: {})".format(self.language.upper()))
            print("3. Find words")
            print("4. Help")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ")
            
            if choice == '1':
                self.enter_letters()
            elif choice == '2':
                self.change_language()
            elif choice == '3':
                self.find_words_menu()
            elif choice == '4':
                self.show_help()
            elif choice == '5':
                print("\nThank you for using Scrabble Word Finder. Goodbye!")
                sys.exit(0)
            else:
                print("\nInvalid choice. Please try again.")
                input("Press Enter to continue...")
    
    # Handle letter input from user.
    def enter_letters(self) -> None:
        self.display_header()
        print("Enter your letters (use '?' for wildcards):")
        letters = input("> ").strip().lower()
        
        # Validate input
        if not letters:
            print("\nNo letters entered. Please try again.")
        elif not all(c.isalpha() or c == WILDCARD_CHAR for c in letters):
            print("\nInvalid input. Only letters and '?' are allowed.")
        else:
            self.letters = letters
            print(f"\nLetters set to: {self.letters}")
        
        input("Press Enter to continue...")
    
    # Handle language selection.
    def change_language(self) -> None:
        self.display_header()
        print("Select language:")
        print("1. English (EN)")
        print("2. Spanish (ES)")
        
        choice = input("\nEnter your choice (1-2): ")
        
        if choice == '1':
            new_language = 'en'
        elif choice == '2':
            new_language = 'es'
        else:
            print("\nInvalid choice. Language not changed.")
            input("Press Enter to continue...")
            return
        
        if new_language != self.language:
            self.language = new_language
            self.dictionary = Dictionary(self.language)
            self.word_finder = WordFinder(self.dictionary)
            print(f"\nLanguage changed to {self.language.upper()}")
        else:
            print("\nLanguage is already set to this option.")
        
        input("Press Enter to continue...")
    
    # Handle word finding with options.
    def find_words_menu(self) -> None:
        if not self.letters:
            print("\nPlease enter letters first.")
            input("Press Enter to continue...")
            return
        
        self.display_header()
        print("Find words with options:")
        print("1. All possible words")
        print("2. Words of specific length")
        print("3. Words with minimum length")
        print("4. Words with maximum length")
        print("5. Back to main menu")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '5':
            return
        
        min_length = 2
        max_length = None
        
        if choice == '1':
            # Use defaults
            pass  
        elif choice == '2':
            try:
                length = int(input("Enter word length: "))
                min_length = max_length = length
            except ValueError:
                print("\nInvalid input. Please enter a number.")
                input("Press Enter to continue...")
                return
        elif choice == '3':
            try:
                min_length = int(input("Enter minimum word length: "))
            except ValueError:
                print("\nInvalid input. Please enter a number.")
                input("Press Enter to continue...")
                return
        elif choice == '4':
            try:
                max_length = int(input("Enter maximum word length: "))
            except ValueError:
                print("\nInvalid input. Please enter a number.")
                input("Press Enter to continue...")
                return
        else:
            print("\nInvalid choice.")
            input("Press Enter to continue...")
            return
        
        # Count wildcards in input
        wildcards = self.letters.count(WILDCARD_CHAR)
        total_wildcards = wildcards if wildcards > 0 else None
        
        # Find and display words
        found_words = self.word_finder.find_words(
            self.letters,
            min_length=min_length,
            max_length=max_length
        )
        
        self.display_header()
        print(f"Searching for words from letters: {self.letters}")
        if min_length == max_length:
            print(f"Word length: {min_length}")
        else:
            print(f"Word length range: {min_length} to {max_length or 'unlimited'}")
        print(f"Wildcards available: {wildcards}")
        
        ScrabbleHelper.display_word_scores(found_words, self.language)
        
        # Additional options after displaying results
        print("\nOptions:")
        print("1. Save results to file")
        print("2. Start new search")
        print("3. Return to main menu")
        
        sub_choice = input("\nEnter your choice (1-3): ")
        
        if sub_choice == '1':
            self.save_results(found_words)
        elif sub_choice == '2':
            self.find_words_menu()
            return
        
        input("Press Enter to continue...")
    
    # Save the found words to a file.
    def save_results(self, words: List[str]) -> None:
        if not words:
            print("\nNo words to save.")
            return
        
        filename = input("Enter filename to save results (default: scrabble_words.txt): ").strip()
        if not filename:
            filename = "scrabble_words.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Letters: {self.letters}\n")
                f.write(f"Language: {self.language}\n")
                f.write(f"Total words: {len(words)}\n\n")
                for word in words:
                    score = ScrabbleHelper.calculate_word_score(word, self.language)
                    f.write(f"{word} - {score} points\n")
            print(f"\nResults saved to {filename}")
        except IOError:
            print("\nError: Could not save file.")
    
    # Display help information.
    def show_help(self) -> None:
        self.display_header()
        print("HELP:")
        print("This tool helps you find all possible Scrabble words from a set of letters.")
        print("\nHow to use:")
        print("1. Enter your letters (use '?' for wildcards/blank tiles)")
        print("2. Choose to find words with various options")
        print("3. View the results with their Scrabble scores")
        print("\nFeatures:")
        print("- Supports both English and Spanish dictionaries")
        print("- Handles wildcards for any letter")
        print("- Filters words by length")
        print("- Calculates Scrabble scores for each word")
        print("- Saves results to a file")
        
        input("\nPress Enter to return to main menu...")

# Entry point for the application.
def main():
    try:
        ui = UserInterface()
        ui.main_menu()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()

# aeplep
# manzana