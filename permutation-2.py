def backtrack(start, nums, curr, result):
  if start == len(nums) and len(curr) == len(nums):
    if curr not in result:
      result.append(curr[:])
    return

  for i in range(start, len(nums)):
    nums[i], nums[start] = nums[start], nums[i]
    backtrack(start + 1, nums, curr + [nums[start]], result)
    nums[i], nums[start] = nums[start], nums[i]


def print_unique_permutations(nums):
  result = []
  backtrack(0, nums, [], result)
  return result

# solution
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))

        return results