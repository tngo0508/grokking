def calculator(expression):
    expr = list(expression)
    expr.append('+')
    stack = []
    sign = '+'
    number = []
    result = 0
    for c in expr:
        if c == ' ':
            continue
        if c.isdigit():
            number.append(c)
        elif c == '+' or c == '-':
            n = int(''.join(number)) if number else 0
            if sign == '+':
                result += n
            else:
                result -= n
            sign = c
            number = []
        elif c == '(':
            stack.append(result)
            stack.append(sign)
            number = []
            result = 0
            sign = '+'
        elif c == ')':
            n = int(''.join(number)) if number else 0
            if sign == '+':
                result += n
            else:
                result -= n

            sign = stack.pop()
            left = stack.pop()
            if sign == '+':
                result = left + result
            else:
                result = left - result
            sign = c
            number = []
    
    return result

# print(calculator("1 + 2"))
# print(calculator("1 + (6 + 2)"))
print(calculator("12 - (6 + 2) + 5"))

# solution
def calculator(expression):
    number = 0
    sign_value = 1
    result = 0
    operation_stack = []

    for c in expression:
        if c.isdigit():
            number = number * 10 + int(c)
        if c in '+-':
            result += number * sign_value
            sign_value = -1 if c == '-' else 1
            number = 0
        elif c == '(':
            operation_stack.append(result)
            operation_stack.append(sign_value)
            result = 0
            sign_value = 1
        elif c == ')':
            result += number * sign_value
            pop_sign_value = operation_stack.pop()
            result *= pop_sign_value

            second_value = operation_stack.pop()
            result += second_value
            number = 0
    
    return result + number * sign_value