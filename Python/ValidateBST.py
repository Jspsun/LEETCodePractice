# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        list = []
        self.inorderTraversal(root, list)
        return self.isInOrder(list)

    def inorderTraversal(self, root, list):
        if root == None:
            return
        self.inorderTraversal(root.left, list)
        list.append(root.val)
        self.inorderTraversal(root.right, list)

    def isInOrder(self, list):
        print list
        for i in range(0, len(list) - 1):
            if list[i] >= list[i + 1]:
                return False
        return True


s = Solution()
from TestObjects import *

root = TreeNode(1)
root.left = TreeNode(1)

b = BinarySearchTree()
print s.isValidBST(root)
