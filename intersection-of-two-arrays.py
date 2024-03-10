# My solution
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = defaultdict(int)
        for num in nums1:
            hash_map[num] = 1
        res = []
        
        for num in nums2:
            if hash_map[num] == 1:
                res.append(num)
                hash_map[num] -= 1
        
        return res

# Approach 2: Built-in Set Intersection
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """  
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)