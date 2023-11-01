def is_palindrome(l, r, s):
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def count_palindromic_substrings(s):
    count = 0
    for i, c in enumerate(s):
        for j in range(i + 1):
            count += is_palindrome(j, i, s)

    return count


# solution
def count_palindromic_substrings(s):
    count = 0

    # Initialize a lookup table of dimensions len(s) * len(s)
    dp = [[False for i in range(len(s))] for i in range(len(s))]
    
    # Base case: A string with one letter is always a palindrome
    for i in range(len(s)):
        dp[i][i] = True
        count += 1

    # Base case: Substrings of two letters
    for i in range(len(s)-1):
        dp[i][i + 1] = (s[i] == s[i + 1])
        # A boolean value is added to the count where True means 1 and False means 0
        count += dp[i][i + 1]

    # Substrings of lengths greater than 2
    for length in range(3, len(s)+1):
        i = 0
        # Checking every possible substring of any specific length
        for j in range(length - 1, len(s)):
            dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
            count += dp[i][j]
            i += 1
    
    return count