from typing import List


class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_string = False


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
        node.val = int(string_to_insert)
    
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

def lexicographical_order(n):
    def dfs(node, output):
        if node.is_string:
            output.append(node.val)

        for i in range(n + 1):
            if str(i) in node.children:
                dfs(node.children[str(i)], output)
            

    trie = Trie()
    for i in range(1, n + 1):
        trie.insert(str(i))
    
    output = []
    dfs(trie.root, output)
    return output

print(lexicographical_order(12))
print(lexicographical_order(15))

def lexicalOrderOptimalSolution(n: int) -> List[int]:
        res = []
        cur = 1
        for i in range(n):
            # Add the current number to the result
            res.append(cur)
            # If the current number times 10 is less than or equal to n, move to the next level
            if cur * 10 <= n:
                cur *= 10
            # Otherwise, move to the next number at the current level
            else:
                # If we've reached the end of a level, divide by 10 to go back up one level
                if cur >= n:
                    cur //= 10
                cur += 1
                # Skip over any trailing zeroes (e.g. if cur = 19, skip over 190, 191, 192, etc.)
                while cur % 10 == 0:
                    cur //= 10
        return res

print(lexicalOrderOptimalSolution(12))
print(lexicalOrderOptimalSolution(15))
print(lexicalOrderOptimalSolution(115))