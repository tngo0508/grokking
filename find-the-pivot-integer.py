# My solution
class Solution:
    def pivotInteger(self, n: int) -> int:
        curr_sum = 0
        total_sum = sum(range(n + 1))
        for i in range(1, n + 1):
            curr_sum += i
            if total_sum - curr_sum + i == curr_sum:
                return i
        return -1

# Editorial Solution
# Approach 2: Two Pointer

class Solution:
    def pivotInteger(self, n: int) -> int:
        left_value = 1
        right_value = n
        sum_left = left_value
        sum_right = right_value

        if n == 1:
            return n

        # Iterate until the pointers meet
        while left_value < right_value:
            # Adjust sums and pointers based on comparison
            if sum_left < sum_right:
                sum_left += left_value + 1
                left_value += 1
            else:
                sum_right += right_value - 1
                right_value -= 1

            # Check for pivot condition
            if sum_left == sum_right and left_value + 1 == right_value - 1:
                return left_value + 1

        return -1  # Return -1 if no pivot is found