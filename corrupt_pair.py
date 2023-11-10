def find_corrupt_pair(nums):
    i = 0
    while i < len(nums):
        x = nums[i] - 1
        if i < len(nums) and i != nums[i] - 1 and nums[i] != nums[x]:
            nums[i], nums[x] = nums[x], nums[i]
            x = nums[i] - 1
        else:
            i += 1

    print(nums)
    res = []
    for i in range(len(nums)):
        if nums[i] - 1 != i:
            res = [i + 1, nums[i]]
        
    return res

print(find_corrupt_pair([4, 1, 2, 1, 6, 3]))