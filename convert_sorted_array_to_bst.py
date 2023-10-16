# Definition of a binary tree node
#
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

from ds_v1.BinaryTree.BinaryTree import TreeNode

def sorted_array_to_bst(nums):
    if not nums:
        return None

    l, r = 0, len(nums) - 1
    m = l + (r - l) // 2
    root = TreeNode(nums[m])
    root.left = sorted_array_to_bst(nums[:m])
    root.right = sorted_array_to_bst(nums[m + 1:])
    return root

####SOLUTION
from TreeNode import *

def sorted_array_to_bst_helper(nums, low, high):
    if(low > high):
        return None;

    mid = low + (high - low) //2 
    root = TreeNode(nums[mid])
    
    root.left = sorted_array_to_bst_helper(nums, low, mid - 1)
    root.right = sorted_array_to_bst_helper(nums, mid + 1, high)

    return root

def sorted_array_to_bst(nums):
    return sorted_array_to_bst_helper(nums, 0, len(nums) - 1)
    
# Driver code
def main():
    
    input_arrays = [
        [11, 22, 33, 44, 55, 66, 77, 88],
        [25, 50, 75, 100, 125, 350],
        [1, 2, 3],
        [1, 2, 3, 4],
        [-10, -3, 0, 5, 9],
        [1, 3]
        
    ]

    indx = 1
    for i in input_arrays:
        
        print(indx, ".\tSorted Array: ", i, sep="")
        indx += 1
        tr = sorted_array_to_bst(i)
        print("\n\tBinary search tree:")
        display_tree(tr)
        print("-"*100)


if __name__ == '__main__':
    main()