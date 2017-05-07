# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    m = {}

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.m = {}
        self.traverse(root)
        freq = max(self.m.values())
        return [e for e in self.m if self.m[e] == freq]

    def traverse(self, root):
        if not root:
            return
        self.traverse(root.left)
        self.traverse(root.right)
        if root.left:
            root.val += root.left.val
        if root.right:
            root.val += root.right.val
        print root.val
        self.m[root.val] = self.m.get(root.val, 0) + 1
