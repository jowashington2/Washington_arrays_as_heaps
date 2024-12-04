class TrieNode:
    """Class representing a single node in the Trie."""
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False  # Marks the end of a word


class Trie:
    """Class representing the Trie data structure."""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Inserts a word into the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """Searches for a word in the Trie and returns True if found, otherwise False."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word


if __name__ == "__main__":
    # Initialize the Trie
    trie = Trie()

    # Words to insert
    words = ["apart", "apple", "bin", "binary", "bit", "byte", "day", "days", "deep", "your_name"]
    your_name = input("Enter your first name: ")
    words.append(your_name.lower())  # Add user's name in lowercase

    # Insert words into the Trie
    for word in words:
        trie.insert(word)

    # Perform searches
    print("\nSearching in the Trie:")
    search_words = ["binary", "pear"]
    for word in search_words:
        result = trie.search(word)
        print(f"Word '{word}': {'Found' if result else 'Not Found'}")
