def helper(s, word_dict, first):
    if first == len(s):
        return True
    
    result = False
    for i in range(first, len(s)):
        word = s[first:i+1]
        if word in word_dict:
            result = helper(s, word_dict, i + 1)

    return result 

def word_break(s, word_dict):
    return helper(s, word_dict, 0)

# solution
