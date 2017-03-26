# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depthMax = 1

        def depth(root):
            if not root:
                return 0
            ansL = depth(root.left)
            ansR = depth(root.right)

            self.depthMax = max(self.depthMax, ansL + ansR + 1)
            return max(ansL, ansR) + 1

        depth(root)
        return self.depthMax - 1
