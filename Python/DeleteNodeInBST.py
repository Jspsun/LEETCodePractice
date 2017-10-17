# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:  
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                root.val = self.getMin(root.right)
                root.right = self.deleteNode (root.right, root.val)
        return root

    def getMin(self, node):
        while node.left:
            node = node.left
        return node.val