# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def containsOne(root):
            if not root:
                return False
            l=containsOne(root.left)
            r=containsOne(root.right)
            if not l:
                root.left = None
            if not r:
                root.right=None
            return root.val== 1 or l or r
        return root if containsOne(root) else None
