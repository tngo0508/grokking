# My solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        count = 0
        for i in range(len(nums)):
            val = nums[i]
            if nums[k] != nums[i]:
                count = count if count < 3 else 2
                while count > 0:
                    k += 1
                    nums[k] = nums[k - 1]
                    count -= 1
                count = 0
            nums[k] = val
            count += 1

        count = count if count < 3 else 2
        while count > 0:
            k += 1
            if k - 1 < 0 or k >= len(nums):
                break
            nums[k] = nums[k - 1]
            count -= 1
        return k
    
# Editorial Solution
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Initialize the counter and the second pointer.
        j, count = 1, 1
        
        # Start from the second element of the array and process
        # elements one by one.
        for i in range(1, len(nums)):
            
            # If the current element is a duplicate, 
            # increment the count.
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                # Reset the count since we encountered a different element
                # than the previous one
                count = 1
            
            # For a count <= 2, we copy the element over thus
            # overwriting the element at index "j" in the array
            if count <= 2:
                nums[j] = nums[i]
                j += 1
                
        return j