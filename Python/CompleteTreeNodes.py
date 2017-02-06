# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = 0
        h = self.getHeight(root)

        while root:
            if self.getHeight(root.right) == h - 1:
                nodes += 2**h
                root = root.right
            else:
                nodes += 2**(h - 1)
                root = root.left
            h -= 1

        return nodes

    def getHeight(self, root):
        if not root:
            return -1
        return 1 + self.getHeight(root.left)
