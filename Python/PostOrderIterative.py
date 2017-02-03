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
        s = []

        if root == None:
            return list

        s.append(root)
        while len(s) > 0:
            x = s.pop()
            if x.left:
                s.append(x.left)
            if x.right:
                s.append(x.right)
            list.append(x.val)
        return list[::-1]
