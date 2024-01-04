# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(nums):
            if not nums:
                return
            l, r = 0, len(nums)
            m = (r + l) // 2
            root = TreeNode(nums[m])
            root.left = helper(nums[:m])
            root.right = helper(nums[m+1:])

            return root

        return helper(nums)