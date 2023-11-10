def first_k_missing_numbers(arr, k):
    i = 0
    while i < len(arr):
        x = arr[i] - 1
        if 0 <= x < len(arr) and i < len(arr) and arr[i] - 1 != i:
            arr[i], arr[x] = arr[x], arr[i]
            x = arr[i] - 1
        else:
            i += 1
    
    missings = []
    set_num = set()

    for i in range(len(arr)):
        if arr[i] - 1 != i:
            set_num.add(arr[i])
            if i not in set_num:
                missings.append(i + 1)
    
    num = len(arr)
    while len(missings) < k:
        missings.append(num + 1)
        num += 1

    return missings

# improved code
def first_k_missing_numbers(arr, k):
    n = len(arr)
    
    # Cyclic sort to bring elements to their correct positions
    i = 0
    while i < n:
        x = arr[i] - 1
        if 0 <= x < n and arr[i] != arr[x]:
            arr[i], arr[x] = arr[x], arr[i]
        else:
            i += 1
    
    missings = []

    # Identify missing numbers
    for i in range(n):
        if arr[i] != i + 1:
            missings.append(i + 1)

    # Append additional missing numbers if needed
    num = n + 1
    while len(missings) < k:
        missings.append(num)
        num += 1

    return missings[:k]