from collections import defaultdict

def is_valid(freq, k):
    most_freq = float('-inf')
    most_freq_char = ""
    replace_count = 0
    for c, count in freq.items():
        if most_freq < count:
            most_freq = count
            most_freq_char = c
    
    for c, count in freq.items():
        if c != most_freq_char:
            replace_count += count
    
    return 0 <= replace_count <= k

def longest_repeating_character_replacement(s, k):
    start, end = 0, 0
    freq = defaultdict(int)
    longest_length = float('-inf')
    while end < len(s):
        c = s[end]
        freq[c] += 1

        if is_valid(freq, k):
            longest_length = max(longest_length, end - start + 1)
        else:
            freq[s[start]] -= 1
            if freq[s[start]] <= 0:
                del freq[s[start]]
            start += 1

        end += 1
    
    return longest_length

print(longest_repeating_character_replacement("aaacbbbaabab", 2))
print(longest_repeating_character_replacement("aaacbbbaabab", 1))