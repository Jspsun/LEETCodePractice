# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # convert to sorted list, sift through differences
        list = []
        self.preOrder(root, list)

        min = list[1] - list[0]
        for i in range(1, len(list)):
            dif = list[i] - list[i - 1]
            if dif < min:
                min = dif
        return min

    def preOrder(self, root, list):
        if root == None:
            return
        self.preOrder(root.left, list)
        list.append(root.val)
        self.preOrder(root.right, list)

from TestObjects import *
b = BinarySearchTree()

S = Solution()
print S.getMinimumDifference(b.root)
