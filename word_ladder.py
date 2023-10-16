from collections import deque

def valid(w1, w2):
    return sum(c1 != c2 for c1, c2 in zip(w1, w2)) == 1

def find_all(word, list_word):
    return [w for w in list_word if valid(w, word)]

def word_ladder(src, dest, words):
    q = deque([[src, 1, set([src])]])
    word_set = set(words)
    list_unique_word = list(word_set)
    while q:
        word, count, curr_set = q.popleft()
        if word == dest:
            return count

        next_words = find_all(word, list_unique_word)
        for next_word in next_words:
            if next_word in curr_set:
                continue
            curr_set.add(next_word)
            q.append([next_word, count + 1, curr_set])
    
    return 0


print(word_ladder("hit" , "cog" , ["hot", "dot", "lot", "log", "cog"]))
# print(word_ladder("hit" , "cog" , ["hot", "dot", "lot", "log", "com"]))