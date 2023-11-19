class TrieNode:
   def __init__(self):
       self.children = {}
       self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        # iterate over each character in the word we want to insert
        for c in word:
            # if the character doesn't belong to any child of the
            # current trie node, then create a new trie node for
            # this character as a child of the current node
            if c not in curr.children:
                curr.children[c] = TrieNode()

            # move to the child of the current node
            # (either already present or just added)
            curr = curr.children[c]
        # set flag end_of_word to TRUE to indicate we've reached
        # the end of inserted word
        curr.end_of_word = True

    # this function replaces each word in the sentence with
    # the smallest word from the dictionary
    def replace(self, word):
        curr = self.root
        # iterate over each dictionary word along
        # with the index of that character
        for i, c in enumerate(word):
            # if the character doesn't belong to the current node's children,
            # then return the word
            if c not in curr.children:
                return word

            # move to the child of the current node
            # corresponding to the current character
            curr = curr.children[c]
            # when the flag end_of_word becomes TRUE, this means
            # we've reached the end of word in the trie. If this is the
            # case, then return this word
            if curr.end_of_word:
                return word[:i+1]
        return word 
def replace_words(sentence, dictionary):
   trie = Trie()
   for word in dictionary:
      trie.insert(word)
   
   words = sentence.split(" ")
   output = []
   for word in words:
      output.append(trie.replace(word))
   
   return " ".join(output)
   
# solution
from trie import Trie


def replace_words(sentence, dictionary):
    trie = Trie()
    
    for prefix in dictionary:
        trie.insert(prefix)
    
    new_list = sentence.split()

    for i in range(len(new_list)):
        
        new_list[i] = trie.replace(new_list[i])

    return " ".join(new_list)


# driver code
def main():

    sentence = ["where there is a will there is a way",
                "the quick brown fox jumps over the lazy dog",
                "oops there is no matching word in this sentence",
                "i was born on twenty ninth february",
                "i dont know where you are but i will find you eventually"]

    dictionary = [["wi", "wa", "w"],
                  ["qui", "f", "la", "d"],
                  ["oops", "there", "is", "no", "matching", "word", "in", "this", "sentence"],
                  ["wa", "w", "a", "ty", "nint", "nin", "n", "feb", "februa", "f"],
                  ["cool", "how", "sunday", 'sun', "x"]]

    for i in range(len(sentence)):
        print(i + 1, ".\t Input sentence: '", sentence[i], "'", sep="")
        print("\t Dictionary words: ", dictionary[i], sep="")
        print("\t After replacing words: '",
              replace_words(sentence[i], dictionary[i]), "'", sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()