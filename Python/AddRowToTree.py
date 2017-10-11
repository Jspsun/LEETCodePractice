# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d ==1:
            temp = TreeNode(v)
            temp.left = root
            return temp
        self.helper(root, v, d)
        return root

    
    def helper (self, root, v, d):
        if not root:
                return
        if d == 2:
            rootLeft = root.left
            rootRight = root.right
            root.left = TreeNode(v)
            root.right = TreeNode(v)
            root.left.left = rootLeft
            root.right.right = rootRight
            return
        self.helper(root.left, v, d-1)
        self.helper(root.right, v, d-1)