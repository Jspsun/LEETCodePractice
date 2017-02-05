# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def __init__(self):
        self.prev = TreeNode(1)

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # preorder traversal
        self.traversal(root)

    def traversal(self, root):
        if not root:
            return
        right = root.right
        self.prev.right = root
        self.prev.left = None
        self.prev = root
        self.traversal(root.left)
        self.traversal(right)
