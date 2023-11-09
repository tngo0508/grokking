def find_missing_number(nums):
    for i in range(len(nums)):
        while nums[i] != i and nums[i] < len(nums):
            index = nums[i]
            nums[i], nums[index] = nums[index], nums[i]

    for i in range(len(nums)):
        if nums[i] != i:
            return i

    # Handle case where no missing number is found
    return len(nums)

# SOLUTION
def find_missing_number(nums):
  len_nums = len(nums)
  index = 0

  while index < len_nums:
    value = nums[index]

    if value < len_nums and value != nums[value]:
      nums[index], nums[value] = nums[value], nums[index]

    elif value >= len_nums:
      index+=1

    else:
      index += 1

  for x in range(len_nums):
    if x != nums[x]:
      return x
  return len_nums