# My solution
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        arr = []
        length_str = ""
        for c in abbr:
            if c.isalpha():
                if len(length_str) > 0:
                    arr.append(length_str)
                arr.append(c)
                length_str = ""
            else:
                if length_str == "" and c == '0':
                    return False
                length_str += c
        
        if len(length_str) > 0:
            arr.append(length_str)

        start = 0
        for elem in arr:
            if elem.isalpha():
                if start >= len(word) or elem != word[start]:
                    return False
                start += 1
            else:
                skip = int(elem)
                start += skip
                if start > len(word):
                    return False
        
        return start >= len(word)


# Clean solution
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            num = 0
            if word[i].isalpha() and abbr[j].isalpha():
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            elif abbr[j] == '0':
                return False
            else:
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num
        return i == len(word) and j == len(abbr)   