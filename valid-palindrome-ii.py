# My Solution
class Solution:
    def validPalindrome(self, s: str) -> bool:
        K = 1
        left, right = 0, len(s) - 1

        def helper(l, r, k):
            if l > r:
                return True

            if k < 0:
                return False

            if s[l] == s[r] and k >= 0:
                return helper(l + 1, r - 1, k)
            else:
                return helper(l + 1, r, k - 1) or helper(l, r - 1, k - 1)

        return helper(left, right, K)