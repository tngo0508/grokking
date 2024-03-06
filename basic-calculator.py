# Brute Force - recursion - Accepted
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        N = len(s)
        def tokenize(expr):
            tokens = []
            i = 0
            curr = ""
            while i < N:
                c = expr[i]
                if c in '+-()':
                    if curr:
                        tokens.append(curr)
                    tokens.append(c)
                    curr = ""
                else:
                    curr += c
                i += 1
            
            if curr:
                tokens.append(curr)

            return tokens

        
        def calc(i, tokens, sign, curr):
            if i == len(tokens) or tokens[i] == ')':
                return curr

            if tokens[i] not in "+-()": # digits
                return calc(i + 1, tokens, sign, sign * int(tokens[i]) + curr)
            
            if tokens[i] in "+-":
                sign = 1 if tokens[i] == "+" else -1
                return calc(i + 1, tokens, sign, curr)
            
            if tokens[i] == '(':
                hash_map = {'(': 1, ')': 0}
                j = i
                while j < len(tokens) and hash_map['('] > 0:
                    j += 1
                    if tokens[j] in '()':
                        hash_map['('] += (1 if tokens[j] == '(' else -1)
                return curr + (calc(i + 1, tokens, 1, 0) * sign) + calc(j + 1, tokens, 1, 0)
            
        
        tokens = tokenize(s)
        return calc(0, tokens, 1, 0)
