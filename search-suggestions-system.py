from pprint import pprint

class TrieNode(object):
    def __init__(self):
        self.search_words = []
        self.children = {}


class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        curr.search_words.append(word)
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.search_words.append(word)
    

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        return curr.search_words[:3]


def suggested_products(products, search_word):
    trie = Trie()
    output = []
    for product in sorted(products):
        trie.insert(product)

    for i in range(1, len(search_word) + 1):
        output.append(trie.search(search_word[:i]))

    return output

print(suggested_products(["bags", "baggage", "banner", "box", "cloths"] , "bags"))

# [["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mouse", "mousepad"], ["mouse", "mousepad"]]
# [["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mouse", "mousepad"], ["mouse", "mousepad"], ["mouse", "mousepad"]]


# [["baggage", "bags", "banner"], ["baggage", "bags", "banner"], ["baggage", "bags", "banner"], ["baggage", "bags"]]
# [["baggage", "bags", "banner"], ["baggage", "bags", "banner"], ["baggage", "bags"], ["bags"]]

# SOLUTION
from trie_node import *

class Trie(object):
    def __init__(self):
        self.root = TrieNode()


    def insert(self, data):
        node = self.root
        idx = 0
        for char in data:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if len(node.search_words) < 3:
                node.search_words.append(data)
            idx += 1

    def search(self, word):
        result, node = [], self.root
        for i, char in enumerate(word):
            if char not in node.children:
                temp = [[] for _ in range(len(word) - i)]
                return result + temp
            else:
                node = node.children[char]
                result.append(node.search_words[:])
        return result


def suggested_products(products, search_word):
    products.sort()
    trie = Trie()
    for x in products:
        trie.insert(x)
    return trie.search(search_word)


# Driver code
def main():
    products = ["bat", "bag", "bassinet", "bread", "cable",
                "table", "tree", "tarp"]
    search_word_list = ["ba", "in", "ca", "t"]
    for i in range(len(search_word_list)):
        print(i + 1, ".\tProducts:", products, sep="")
        print("\tSearch keyword: '", search_word_list[i], "'", sep="")
        print("\tSuggested Products: ", suggested_products(
            products, search_word_list[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()
