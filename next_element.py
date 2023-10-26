def next_greater_element(nums1, nums2):
    res = []
    stack = []
    hash_map = {}
    for num in nums2:
        while stack and num > stack[-1]:
            x = stack.pop()
            hash_map[x] = num
        stack.append(num)

    for num in nums1:
        res.append(hash_map.get(num, -1))

    return res


print(next_greater_element([137, 59, 92, 122, 52, 131, 79, 236], [
      137, 59, 92, 122, 52, 131, 79, 236]))
