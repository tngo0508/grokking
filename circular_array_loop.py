import unittest


def get_next_idx(index, nums):
    return (index + nums[index]) % len(nums)


def is_direction_changed(val1, val2):
    return val1 * val2 < 0


def is_not_cycle(slow_idx, fast_idx, next_slow_idx, next_fast_idx, nums):
    if is_direction_changed(nums[slow_idx], nums[next_slow_idx]):
        return True

    if is_direction_changed(nums[fast_idx], nums[next_fast_idx]):
        return True

    return False


def circular_array_loop(nums):
    if not nums:
        return False

    curr_idx = 0
    while curr_idx < len(nums):
        slow_idx = curr_idx
        fast_idx = curr_idx
        while slow_idx < len(nums) and fast_idx < len(nums):
            next_slow_idx = get_next_idx(slow_idx, nums)
            next_fast_idx = get_next_idx(get_next_idx(fast_idx, nums), nums)

            if is_not_cycle(slow_idx, fast_idx, next_slow_idx, next_fast_idx, nums):
                break

            slow_idx = next_slow_idx
            fast_idx = next_fast_idx

            if slow_idx == fast_idx:
                return True

        curr_idx += 1
    return False


class TestStringMethods(unittest.TestCase):
    test_data = [
        ([1, 3, -2, -4, 1], True),
        ([2, 1, -1, -2], False),
        ([5, 4, -2, -1, 3], False),
        ([1, 2, -3, 3, 4, 7, 1], True),
        ([3, 3, 1, -1, 2], True),
    ]
    def test(self):
        for data, result in self.test_data:
            self.assertTrue(circular_array_loop(data))


if __name__ == '__main__':
    unittest.main()
