def min_remove_parentheses(s):
    stack = []
    for i, c in enumerate(s):
        if c not in '()':
            continue
        if c == '(':
            stack.append(['(', i])
        else:
            if stack and stack[-1][0] == '(':
                stack.pop()
            else:
                stack.append([')', i])
    
    removed_list = [i for _, i in stack]
    result = []
    for i, c in enumerate(s):
        if i not in removed_list:
            result.append(c)
    return ''.join(result)


print(min_remove_parentheses("ab)ca(so)(sc(s)("))
print(min_remove_parentheses(")))(((("))

# solution
def min_remove_parentheses(s):
    stack = []
    s_list = list(s)
    
    for i, val in enumerate(s):
        if len(stack) > 0 and stack[-1][0] == '(' and val == ')':
            stack.pop()

        elif val == '(' or val == ')':
            stack.append([val, i])

    for p in stack:
        s_list[p[1]] = ""
    
    result = ''.join(s_list)
   
    return result