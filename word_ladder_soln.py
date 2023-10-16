def word_ladder(src, dest, words):
    myset = set(words)

    if dest not in myset:
        return 0

    q = []
    q.append(src)
    length = 0

    while q:
        length += 1
        size = len(q)

        for _ in range(size):
            curr = q.pop(0)

            for i in range(len(curr)):
                alpha = "abcdefghijklmnopqrstuvwxyz"
       
                for c in alpha:
                    temp = list(curr)
                    temp[i] = c
                    temp = "".join(temp)
 
                    if temp == dest:
                        return length + 1

                    if temp in myset:
                        q.append(temp)
                        myset.remove(temp)
    return 0

# Driver code
if __name__ == '__main__':
	
	words_list = [["hog", "dot", "pot", "pop", "mop", "map", "cap", "cat"],["hot","dot","lot","log","cog"],["hot","not","dot","lot","cog"], ["hog","dot","pot","pop","mop","map","cap","cat"], ["hot", "dot", "lot", "log", "cog","com","cam","frog"]]
	src_list = ["dog", "hit", "hat", "dog", "dog"]
	dest_list = ["cat", "cog", "log", "cat", "frog"]
    
for i in range(len(src_list)):
    print(i + 1, ".\tsrc: \"", src_list[i], "\"", sep = "")
    print("\tdest: \"", dest_list[i], "\"", sep = "")
    print("\tAvailable words: ", words_list[i], "\n",sep = "")
    print("\tLength of shortest chain is: ",word_ladder(src_list[i], dest_list[i], words_list[i]))        
    print("-" * 100)