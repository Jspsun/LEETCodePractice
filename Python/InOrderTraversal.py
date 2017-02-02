# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list = []
        return self.helper(root, list)

    def helper(self, root, list):
        if root == None:
            return []
        self.helper(root.left, list)
        list.append(root.val)
        self.helper(root.right, list)
        return list
