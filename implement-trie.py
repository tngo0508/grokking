class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    # inserting string in trie
    def insert(self, string):
        curr = self.root
        for c in string:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True
    
    # searching for a string
    def search(self, string):
        curr = self.root
        for c in string:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.is_word
    
    # searching for a prefix
    def search_prefix(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

# SOLUTION
from trie_node import *

class Trie():
    # Constructor to create a trie node.
    def __init__(self):
        self.root = TrieNode()

    # A function to insert a word in trie.
    def insert(self, word):
        node = self.root
        
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children.get(c)
        
        node.is_word = True  

    # A function to search for a word in the trie.
    def search(self, word):
        node = self.root
        
        for c in word:
            if c not in node.children:
                return False
            node = node.children.get(c)

        return node.is_word

    # A function to search for a prefix of a word in the trie.
    def search_prefix(self, prefix):
        node = self.root

        for c in prefix:
            if c not in node.children:
                return False
            node = node.children.get(c)

        return True


# Driver Code
def main():
    keys = ["the", "a", "there", "answer"]
    trie_for_keys = Trie()
    num = 1
    for x in keys:
        print(num, ".\tInsert key: '", x, "'", sep="")
        trie_for_keys.insert(x)
        num += 1
        print("-" * 100)

    search = ["a", "answer", "xyz", "an"]
    for y in search:
        print(num, ".\tSearch key: '", y, "'", sep="")
        print("\tKey found? ", trie_for_keys.search(y), sep="")
        num += 1
        print("-" * 100)

    searchPrefix = ["b", "an"]
    for z in searchPrefix:
        print(num, ".\tSearch prefix: '", z, "'", sep="")
        print("\tPrefix found? ", trie_for_keys.search_prefix(z), sep="")
        num += 1
        print("-" * 100)


if __name__ == "__main__":
    main()
