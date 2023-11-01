from collections import Counter, defaultdict

def helper(nums, target, first, result, curr):
    if first == len(nums):
        return
    
    if sum(curr) > target:
        return

    if sum(curr) == target:
        temp = list(sorted(curr))
        if temp not in result:
            print(temp)
            result.append(temp[:])
        return

    for i in range(first, len(nums)):
        num = nums[i]
        helper(nums, target, i, result, curr + [num])

    


def combination_sum(nums, target):
    result = []
    helper(nums, target, 0, result, [])
    return result


# solution
def combination_sum(nums, target):
    # Initialize dp
    dp = [[] for _ in range(target + 1)]
    dp[0].append([])

    # For each value from 1 to target
    for i in range(1, target + 1):
        # Iterate over nums
        for j in range(len(nums)):
            if nums[j] <= i:

                # Check previous results from dp
                for prev in dp[i - nums[j]]:
                    temp = prev + [nums[j]]
                    temp.sort()
                    # If the new combination is not already in dp
                    if temp not in dp[i]:
                        dp[i].append(temp)
    # Return the combinations
    return dp[target]


print(combination_sum([2,4,7,9,11], 8))