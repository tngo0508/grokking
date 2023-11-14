from collections import defaultdict, Counter, deque

def alien_order(words):
    adj_list = defaultdict(set)
    counts = Counter({c: 0 for word in words for c in word})
    outer = 0
    for word1, word2 in zip(words, words[1:]):
        outer += 1
        inner = 0
        for c, d in zip(word1, word2):
            inner += 1
            if c != d:
                if d not in adj_list[c]:
                    adj_list[c].add(d)
                    counts[d] += 1
                break

        else:  
            if len(word2) < len(word1):
                return ""

    
    result = []
    sources_queue = deque([c for c in counts if counts[c] == 0])
    while sources_queue:
        c = sources_queue.popleft()
        result.append(c)

        for d in adj_list[c]:
            counts[d] -= 1
            if counts[d] == 0:
                sources_queue.append(d)

    if len(result) < len(counts):
        return ""
    return "".join(result)


# Driver code
def main():
    words = [
        ["mzosr", "mqov", "xxsvq", "xazv", "xazau", "xaqu",
            "suvzu", "suvxq", "suam", "suax", "rom", "rwx", "rwv"],
        ["vanilla", "alpine", "algor", "port",
            "norm", "nylon", "ophellia", "hidden"],
        ["passengers", "to", "the", "unknown"],
        ["alpha", "bravo", "charlie", "delta"],
        ["jupyter", "ascending"]]

    for i in range(len(words)):
        print(i + 1, ".\twords = ", words[i], sep="")
        print("\tDictionary = \"", alien_order(words[i]), "\"", sep="")
        print("-"*100)


if __name__ == "__main__":
    main()

# leetcode solution
class Solution:
    def alienOrder(self, words: List[str]) -> str:  
        # Step 0: create data structures + the in_degree of each unique letter to 0.
        adj_list = defaultdict(set)
        in_degree = Counter({c : 0 for word in words for c in word})
                
        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): return ""
        
        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)
                    
        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(in_degree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output)