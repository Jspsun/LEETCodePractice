# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution(object):

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        list = []
        self.levelMaker(list, root, 0)
        return list

    def levelMaker(self, list, root, level):
        if root == None:
            return
        if level >= len(list):
            list.insert(0, [])
        list[len(list) - level - 1].append(root.val)
        self.levelMaker(list, root.left, level + 1)
        self.levelMaker(list, root.right, level + 1)


from TestObjects import *

b = BinaryTree()
s = Solution()
print s.levelOrderBottom(b.root)
