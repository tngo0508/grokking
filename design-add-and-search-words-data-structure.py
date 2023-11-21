# TrieNode template class
class TrieNode():
  
  # Initialize TrieNode instance
  def __init__(self):
    # Empty list of child nodes
    self.children = []
    # False indicates this node is not the end of a word
    self.complete = False
    # Create 26 child nodes for each letter of alphabet
    for i in range(0, 26):
      self.children.append(None)


class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    # Function to insert a string in the trie
    def insert(self, string_to_insert):
        node = self.root
        for c in string_to_insert:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children.get(c)
        node.complete = True
    
    # Function to search a string from the trie
    def search(self, string_to_search):
        node = self.root
        for c in string_to_search:
            if c not in node.children:
                return False
            node = node.children.get(c)
        return node.complete
    
    # Function to search prefix of strings
    def starts_with(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children.get(c)
        return True
    
# solution
from trie_node import *


class WordDictionary:
    # Initialize the root with TrieNode and set 
    # the 'can_find' boolean to FALSE
    def __init__(self):
        self.root = TrieNode()
        self.can_find = False


    # Function to add a new word to the dictionary
    def add_word(self, word):
        n = len(word)
        cur_node = self.root
        for i, val in enumerate(word):
            # Find the correct index of the character in the list of nodes
            index = ord(val) - ord('a')
            # If the letter is not present in the trie, then 
            # create a new trie node for it, 
            # otherwise use the existing trie node for this letter
            if cur_node.children[index] is None:
                cur_node.children[index] = TrieNode()
            cur_node = cur_node.children[index]
            if i == n - 1:
                # If we've reached the end of word and complete flag is already set
                # this means that it is already present in the dictionary
                if cur_node.complete:
                    print("\tWord already present!")
                    return
                # Once all the characters are added to the trie, 
                # set the 'complete' variable to TRUE
                cur_node.complete = True
        print("\tWord added successfully!")


    # Function to search for a word in the dictionary
    def search_word(self, word):
        # Set the 'can_find' variable as FALSE
        self.can_find = False
        # Perform depth-first search to iterate over the children nodes
        self.search_helper(self.root, word, 0)
        return self.can_find


    def search_helper(self, node, word, i):
        # If the word has already been found and there is no need 
        # for further searching, return the control to the calling context
        if self.can_find:
            return
        # Return the control to the calling context 
        # if the current node is empty
        if not node:
            return
        # If we have found the last character of the query string
        # in the trie and the complete flag is set, we have found the entire word
        if len(word) == i:
            if node.complete:
                self.can_find = True
            return

        # If the word contains a wildcard character ".", match
        # it with all of the children (letters) of the current node and
        # perform depth first search starting at each child
        if word[i] == '.':
            for j in range(ord('a'), ord('z') + 1):
                self.search_helper(node.children[j - ord('a')], word, i + 1)
        else:
            # otherwise, simply locate the child corresponding to the current character
            index = ord(word[i]) - ord('a')
            # and continue the depth-first traversal
            self.search_helper(node.children[index], word, i + 1)


    # Function to get all words in the dictionary
    def get_words(self):
        words_list = []
        # Return an empty list if the root is NULL
        if not self.root:
            return []
        # Perform depth first search on the trie
        return self.dfs(self.root, "", words_list)

    def dfs(self, node, word, words_list):
        # If the node is NULL, return the 'words_list'
        if not node:
            return words_list
        # If the word is complete, add it to the 'words_list'
        if node.complete:
            words_list.append(word)

        for j in range(ord('a'), ord('z') + 1):
            prefix = word + chr(j)
            words_list = self.dfs(node.children[j - ord('a')], prefix, words_list)
        return words_list


# Driver code
def main():
    obj = WordDictionary()
    # Adding words
    words = ["add", "sky", "hello", "multi", "addition", "sky", "multiply", "table"]
    i = 1
    for w in words:
        print(i, ".\tAdding word: '", w, "'", sep="")
        obj.add_word(w)
        print("-" * 100, sep="")
        i += 1

    # Searching words
    wordSearch = ["helo", "multiple", "...le", "..llo", "..r"]
    for v in wordSearch:
        print(i, ".\tSearching word: '", v, "'", sep="")
        print("\t", obj.search_word(v), sep="")
        print("-" * 100, sep="")
        i += 1

    # Getting all words
    print(i, ".\tGetting all words: ", obj.get_words(), sep="")
    print("-" * 100, sep="")


if __name__ == "__main__":
    main()

# rewrite so i can understand
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        curr = self.root
        for c in word:
            index = ord(c.lower()) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.complete = True

    def search_word(self, word):
        def helper(word, node):
            for i, c in enumerate(word):
                index = ord(c.lower()) - ord('a')
                if not (0 <= index < 26) or not node.children[index]:
                    if c == '.':
                        for j in range(26):
                            if node.children[j] and helper(word[i + 1:], node.children[j]):
                                return True
                        return False
                else:
                    node = node.children[index]
            
            return node.complete

        return helper(word, self.root)

    def get_words(self):
        def dfs(node, word, output):
            if not node:
                return output
            
            if node.complete:
                output.append(word)
            
            for i in range(26):
                prefix = word + chr(i + ord('a'))
                output = dfs(node.children[i], prefix, output)
            
            return output


        output = []
        if not self.root:
            return []
        return dfs(self.root, "", output)
        



