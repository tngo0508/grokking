def jump_game(nums):
    target = len(nums) - 1
    i = len(nums) - 2
    while i >= 0:
        if i == 0 and nums[i] + i < target:
            return False
        if nums[i] + i >= target:
            target = i
            i = target - 1
        else:
            i -= 1
    return True
        

        
