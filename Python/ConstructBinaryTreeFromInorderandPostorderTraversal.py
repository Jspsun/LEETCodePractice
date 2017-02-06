# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root = TreeNode(postorder.pop())
        index = inorder.index(root.val)
        # passes in the values for everything right of the root
        # if the tree is done building for that side, the inorder list is empty
        root.right = self.buildTree(inorder[index + 1:], postorder)
        # passes in the values for everything left of the root
        # if the tree is done building for that side, the inorder list is empty
        root.left = self.buildTree(inorder[:index], postorder)
        return root
