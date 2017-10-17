# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        s = set([])
        return self.dfs(root, s, k)
    
    def dfs (self, root, set, target):
        if not root:
            return False
        if target-root.val in set:
            return True
        set.add(root.val)
        return self.dfs(root.left, set, target) or self.dfs(root.right,set, target)
