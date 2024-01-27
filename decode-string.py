class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ']':
                curr = ''
                while stack and stack[-1] != '[':
                    curr = stack.pop() + curr
                
                stack.pop()
                num_str = ''
                while stack and stack[-1].isdigit():
                    num_str = stack.pop() + num_str
                num = int(num_str)
                stack.append(num * curr)
            else:
                stack.append(c)
        
        return ''.join(stack)
        