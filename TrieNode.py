class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes
        self.children = {}  
        # Marks the end of a complete word
        self.is_end_of_word = False  


# A recursive implementation of the Trie (Prefix Tree) data structure.
# Supports insertion, search, and prefix checking operations.
class RecursiveTrie:
    # Initialize the Trie with a root node.
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into the Trie.
    def insert(self, word):
        self._insert_recursive(self.root, word, 0)

    # Helper method to recursively insert a word into the Trie.
    def _insert_recursive(self, node, word, index):
        if index == len(word):
            # Mark the end of the complete word
            node.is_end_of_word = True
            return

        char = word[index]
        if char not in node.children:
            # Create a new node if the character doesn't exist
            node.children[char] = TrieNode()

        # Recursively insert the remaining characters
        self._insert_recursive(node.children[char], word, index + 1)

    # Search for a complete word in the Trie.
    def search(self, word):
        return self._search_recursive(self.root, word, 0)

    # Helper method to recursively search for a word in the Trie.
    def _search_recursive(self, node, word, index):
        if index == len(word):
            # We've reached the end of the word, check if it's marked as complete
            return node.is_end_of_word

        char = word[index]
        if char not in node.children:
            # Character not found in current node's children
            return False

        # Recursively search the remaining characters
        return self._search_recursive(node.children[char], word, index + 1)

    # Check if any word in the Trie starts with the given prefix.
    def starts_with(self, prefix):
        return self._starts_with_recursive(self.root, prefix, 0)

    # Helper method to recursively check for a prefix in the Trie.
    def _starts_with_recursive(self, node, prefix, index):
        # If we've reached the end of the prefix, it means it's found
        if index == len(prefix):
            # We've successfully matched all characters of the prefix
            return True

        char = prefix[index]
        if char not in node.children:
            # Character not found in current node's children
            return False

        # Recursively check the remaining characters of the prefix
        return self._starts_with_recursive(node.children[char], prefix, index + 1)


# Example usage
if __name__ == "__main__":
    trie = RecursiveTrie()
    
    # Insert words into the Trie
    words = ["apple", "app", "application", "banana", "ball"]
    for word in words:
        trie.insert(word)
        print(f"Inserted: {word}")
    
    # Search for words in the Trie
    search_words = ["app", "apple", "apples", "ban", "ball"]
    for word in search_words:
        if trie.search(word):
            print(f"Found word: {word}")
        else:
            print(f"Word not found: {word}")
    
    # Check for prefixes
    prefixes = ["app", "ban", "cat", "bal"]
    for prefix in prefixes:
        if trie.starts_with(prefix):
            print(f"Found prefix: {prefix}")
        else:
            print(f"Prefix not found: {prefix}")