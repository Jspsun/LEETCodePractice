# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        val = []
        self.recurse(root, 0, val)
        return val[-1]

    def recurse(self, root, level, values):
        if not root:
            return
        if len(values) < level + 1:
            values.append(root.val)
        else:
            values[level] = root.val
        self.recurse(root.right, level + 1, values)
        self.recurse(root.left, level + 1, values)
