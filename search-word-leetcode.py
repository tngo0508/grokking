class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr["is_word"] = True

    def search(self, word: str) -> bool:
        def helper(word, node):
            for i, c in enumerate(word):
                if c not in node:
                    if c == '.':
                        for x in node:
                            if x != "is_word" and helper(word[i + 1:], node[x]):
                                return True
                    return False
                else:
                    node = node[c]
            return "is_word" in node
        
        return helper(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)