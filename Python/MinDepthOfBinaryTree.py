# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        list = [99999]
        self.helper(root, 1, list)
        return list[0]

    def helper(self, root, level, lowest):
        if root.left == None and root.right == None:
            if level < lowest[0]:
                lowest[0] = level
            return
        if root.left:
            self.helper(root.left, level + 1, lowest)
        if root.right:
            self.helper(root.right, level + 1, lowest)

from TestObjects import BinaryTree
s = Solution()
b = BinaryTree()
print s.minDepth(b.root)
