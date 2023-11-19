from typing import List

class Solution:
    @staticmethod
    def subsets(nums: List[int]) -> List[List[int]]:
        output = [[]]
        for num in nums:
            curr = []
            for x in output:
                curr.append(x[:])
            for i in range(len(curr)):
                curr[i].append(num)
            for x in curr:
                output.append(x[:])
        return output
        

print(Solution.subsets([1,2,3]))

# leetcode solution - backtrack
def backtrack(first = 0, curr = []):
    if first == k:
        output.append(curr[:])
        return
    
    for i in range(first, len(nums)):
        backtrack(i + 1, curr + [nums[i]])

    output = []
    for k in range(len(nums) + 1):
        backtrack()

    return output