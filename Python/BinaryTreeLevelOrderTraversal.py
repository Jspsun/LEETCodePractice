# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        list = []
        self.helper(list, root, 0)
        return list

    def helper(self, list, root, level):
        if root == None:
            return
        if level >= len(list):
            list.append([])
        list[level].append(root.val)
        self.helper(list, root.left, level + 1)
        self.helper(list, root.right, level + 1)

from TestObjects import BinaryTree
b = BinaryTree()
s = Solution()
print s.levelOrder(b.root)
