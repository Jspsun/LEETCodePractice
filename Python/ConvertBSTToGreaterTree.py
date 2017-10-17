# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    lower = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.convert(root)
        return root
    
    def convert(self, root):
        if not root:
            return

        self.convert(root.right)
        root.val +=self.lower
        self.lower = root.val
        self.convert(root.left)