# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    list = []

    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.list = []
        self.dfs(root, 0)
        return self.list

    def dfs(self, root, level):
        if root == None:
            return
        if len(self.list) <= level:
            self.list.append(root.val)
        if root.val > self.list[level]:
            self.list[level] = root.val
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)

S = Solution()
from TestObjects import *
print S.largestValues(BinaryTree().root)
