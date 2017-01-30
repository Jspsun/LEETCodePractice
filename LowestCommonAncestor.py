# Definition for a binary tree node.
# class TreeNode(object):
#
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if (root.val >= p.val and root.val <= q.val) or (root.val <= p.val and root.val >= q.val):
            return root
        if root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p, q)

from TestObjects import *

b = BinarySearchTree()
p = TreeNode(0)
q = TreeNode(5)
s = Solution()
print s.lowestCommonAncestor(b.root, p, q).val
