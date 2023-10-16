def jump_game_two(nums):
    farthest_jump = 0
    curr_jump = 0
    jump = 0
    for i, num in enumerate(nums):
        if curr_jump >= len(nums) - 1:
            break
        farthest_jump = max(farthest_jump, num + i)
        if i == curr_jump:
            jump += 1
            curr_jump = farthest_jump
    return jump