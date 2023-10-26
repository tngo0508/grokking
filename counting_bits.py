def counting_bits(n):
    result = [0] * (n + 1)
    for i in range(n + 1):
        num = i
        temp = 0
        while num > 0:
            temp += num & 1
            num = num >> 1
        result[i] = temp
    return result

# solution
def counting_bits(n):
    result = [0] * (n + 1)

    if n == 0:
        return result

    result[0] = 0
    result[1] = 1

    for x in range(2, n + 1):
        if x % 2 == 0:
            result[x] = result[x // 2]
        else:
            result[x] = result[x // 2] + 1

    return result
