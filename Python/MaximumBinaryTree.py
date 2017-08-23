# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        
        max = 0
        for i in range(len(nums)):
            if nums[i] > nums[max]:
                max  = i
        newNode = TreeNode(nums[max])
        newNode.left = self.constructMaximumBinaryTree(nums[:max])
        newNode.right = self.constructMaximumBinaryTree(nums[max+1:])
        return newNode
    