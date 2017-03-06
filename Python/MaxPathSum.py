# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    maxVal = 0

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxVal = -9999999
        self.maxPathDown(root)
        return self.maxVal

    # computes the max path down
    # the path starts with input node
    def maxPathDown(self, root):
        if not root:
            return 0
        left = max(0, self.maxPathDown(root.left))
        right = max(0, self.maxPathDown(root.right))
        self.maxVal = max(self.maxVal, left + right + root.val)
        # adds to the current value of the path
        return max(left, right) + root.val
