class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_string = False
        self.val = ""

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
        node.is_string = True
        node.val = string_to_insert
    
    # Function to search a string from the trie
    def search(self, string_to_search):
        node = self.root
        for c in string_to_search:
            if c not in node.children:
                return False
            node = node.children.get(c)
        return node.is_string
    
    # Function to search prefix of strings
    def starts_with(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children.get(c)
        return True

    # Function to delete the characters in the searched word that are not shared
    def remove_characters(self, string_to_delete):
        node = self.root
        child_list = []
    
        for c in string_to_delete:
            child_list.append([node, c])
            node = node.children[c]
        
        for pair in reversed(child_list):
            parent = pair[0]
            child_char = pair[1]
            target = parent.children[child_char]

            if target.children:
                return
            del parent.children[child_char]


def find_strings(grid, words):
    def backtrack(row, col, node):
        letter = grid[row][col]
        curr = node.children.get(letter)
    
        if curr.is_string:
            output.append(curr.val)
            curr.is_string = False

        grid[row][col] = '#'

        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            r = x + row
            c = y + col
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] in curr.children:
                backtrack(r, c, curr)

        grid[row][col] = letter

        # Optimization: incrementally remove the matched leaf node in Trie.
        if not node:
            node.children.pop(letter)


    trie = Trie()
    for word in words:
        trie.insert(word)

    output = []

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] in trie.root.children:
                backtrack(row, col, trie.root)

    return output

# print(find_strings([["C", "S", "L", "I", "M"], ["O", "I", "L", "M", "O"], ["O", "L", "I", "E", "O"], ["R", "T", "A", "S", "N"], ["S", "I", "T", "A", "C"]] , ["SLIME", "SAILOR", "MATCH", "COCOON"]))
print(find_strings([["C", "O", "L", "I", "M"], ["I", "N", "L", "M", "O"], ["A", "L", "I", "E", "O"], ["R", "T", "A", "S", "N"], ["S", "I", "T", "A", "C"]] , ["REINDEER", "IN", "RAIN"]))