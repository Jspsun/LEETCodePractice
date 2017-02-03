# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list = []
        self.helper(root, list)
        return list

    def helper(self, root, list):
        if not root:
            return
        self.helper(root.left, list)
        self.helper(root.right, list)
        list.append(root.val)

from TestObjects import *
s = Solution()
b = BinaryTree()
print s.postorderTraversal(b.root)
