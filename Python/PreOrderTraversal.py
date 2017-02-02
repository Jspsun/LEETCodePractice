# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list = []
        self.helper(root, list)
        return list

    def helper(self, root, list):
        if root == None:
            return
        list.append(root.val)
        self.helper(root.left, list)
        self.helper(root.right, list)
