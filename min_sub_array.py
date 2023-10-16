def min_sub_array_len(target, nums):
    start = 0
    curr_sum = 0
    result = 0
    for end in range(len(nums)):
        curr_sum += nums[end]
        while curr_sum >= target and start <= end:
            result = end - start + 1
            curr_sum -= nums[start]
            start += 1
    
    return result