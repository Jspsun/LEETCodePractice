# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s or not t:
            return False
        if s.val == t.val:
            if self.isSame(s, t):
                return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSame(self, sN, tN):
        if not sN and not tN:
            return True
        if not sN or not tN:
            return False
        if sN.val != tN.val:
            return False
        return self.isSame(sN.left, tN.left) and self.isSame(sN.right, tN.right)
