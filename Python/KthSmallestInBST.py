# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # in order traversal, append to List
        # get kth item
        list = []
        list = self.inOrderTraversal(root, list)
        return list[k - 1]

    def inOrderTraversal(self, root, list):
        if root == None:
            return
        self.inOrderTraversal(root.left, list)
        list.append(root.val)
        self.inOrderTraversal(root.right, list)
        return list

s = Solution()
from TestObjects import BinarySearchTree
b = BinarySearchTree()
print s.kthSmallest(b.root, 2)
