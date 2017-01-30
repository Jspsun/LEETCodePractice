# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution(object):

    def levelOrderBottom(self, root):
        list = []
        self.helper(list, root, 0)
        return list[::-1]

    def helper(self, list, root, level):
        if root == None:
            return
        if level >= len(list):
            list.append([])
        list[level].append(root.val)
        self.helper(list, root.left, level + 1)
        self.helper(list, root.right, level + 1)


from TestObjects import *

b = BinaryTree()
s = Solution()
print s.levelOrderBottom(b.root)
