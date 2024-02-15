# My solution
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        hash_map = defaultdict(int)
        for word in words:
            hash_map[word] = len(word)
        
        res = []
        curr = []
        available_spaces = maxWidth
        for word in words:
            if available_spaces - hash_map[word] == 0:
                available_spaces -= hash_map[word]
            else:
                available_spaces -= (hash_map[word] + 1)

            if available_spaces >= 0:
                curr.append(word)
            else:
                if curr:
                    res.append(curr[:])
                available_spaces = maxWidth
                available_spaces -= (hash_map[word] + 1)
                curr = [word]
        
        if curr:
            res.append(curr[:])

        for i in range(len(res) - 1):
            arr = res[i]
            num_of_chars = 0
            num_of_words = len(arr)
            for s in arr:
                num_of_chars += hash_map[s]
            
            spaces = maxWidth - num_of_chars
            spaces_in_between = spaces // (num_of_words - 1) if num_of_words > 1 else 0
            spaces_left = spaces % (num_of_words - 1) if num_of_words > 1 else 0
            for j in range(spaces_left):
                arr[j] = ''.join(list(arr[j]) + [' '])
            
            if spaces_in_between > 0:
                delimiter = ' ' * spaces_in_between
                res[i] = str(delimiter.join(arr))
            else:
                res[i] = str(''.join(arr))
                if len(res[i]) < maxWidth:
                    res[i] += ' ' * (maxWidth - len(res[i]))

        
        if res:
            res[-1] = str(' '.join(res[-1]))
            if len(res[-1]) < maxWidth:
                res[-1] += ' ' * (maxWidth - len(res[-1]))

        return res
