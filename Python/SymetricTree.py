# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False

        return (left.val == right.val) and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

s = Solution()
from TestObjects import SymetricBinaryTree
b = SymetricBinaryTree()
print s.isSymmetric(b.root)
