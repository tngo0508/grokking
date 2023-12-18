class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(i, open, n, result, curr):
            if open > n or open < 0:
                return
            
            if i == n * 2:
                if open == 0:
                    result.append(''.join(curr))
                return
            for c in '()':
                if c == '(':
                    backtrack(i + 1, open + 1,  n, result, curr + [c])
                else:
                    backtrack(i + 1, open - 1, n, result, curr + [c])

        result = []
        backtrack(0, 0, n, result, [])
        return result
    

# Solution
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(p_string):
            left_count = 0
            for p in p_string:
                if p == '(':
                    left_count += 1
                else:
                    left_count -= 1

                if left_count < 0:
                    return False
                
            return left_count == 0
        
        answer = []
        queue = collections.deque([""])
        while queue:
            cur_string = queue.popleft()

            # If the length of cur_string is 2 * n, add it to `answer` if
            # it is valid.
            if len(cur_string) == 2 * n:
                if isValid(cur_string):
                    answer.append(cur_string)
                continue
            queue.append(cur_string + ")")
            queue.append(cur_string + "(")
            
        return answer
    
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def backtracking(cur_string, left_count, right_count):
            if len(cur_string) == 2 * n:
                answer.append("".join(cur_string))
                return
            if left_count < n:
                cur_string.append("(")
                backtracking(cur_string, left_count + 1, right_count)
                cur_string.pop()
            if right_count < left_count:
                cur_string.append(")")
                backtracking(cur_string, left_count, right_count + 1)
                cur_string.pop()
        backtracking([], 0, 0)
        return answer