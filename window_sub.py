def min_window(str1, str2):
    if len(str2) == 0:
        return ""
    
    length = 0
    result = ""
    min_length = float('inf')
    for i in range(len(str1)):
        if str1[i] == str2[0]:
            idx_1 = i
            idx_2 = 0
            for idx_1 in range(i, len(str1)):
                if str1[idx_1] == str2[idx_2]:
                    idx_2 += 1
                curr_length = idx_1 - i + 1
                if idx_2 == len(str2):
                    if curr_length < min_length:
                        min_length = curr_length
                        result = str1[i:idx_1 + 1]
                    idx_2 = 0
    
    return result

print(min_window("abcdebdde", "bde"))