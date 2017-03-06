# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    total = 0

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total = 0
        self.dfs(root, 0)
        return self.total

    def dfs(self, root, temp):
        if not root:
            return
        temp = temp * 10 + root.val
        if not root.left and not root.right:
            self.total += temp
            return
        self.dfs(root.left, temp)
        self.dfs(root.right, temp)
