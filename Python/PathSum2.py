# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        list = []
        master = []
        self.helper(root, list, master, 0, sum)
        return master

    def helper(self, root, list, master, currentSum, targetSum):
        if not root:
            return
        list.append(root.val)
        currentSum += root.val
        if not root.left and not root.right:
            if currentSum == targetSum:
                master.append(list)
            return
        self.helper(root.left, list[:], master, currentSum, targetSum)
        self.helper(root.right, list[:], master, currentSum, targetSum)
