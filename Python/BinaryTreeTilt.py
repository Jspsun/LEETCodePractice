# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# my o(n)Solution
class Solution(object):
    tilt = 0

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def postOrderTrav(root):
            if not root:
                return 0
            left = postOrderTrav(root.left)
            right = postOrderTrav(root.right)
            self.tilt += abs(left - right)
            return root.val + left + right

        postOrderTrav(root)
        return self.tilt

# This one is o(n^2) and naive so I'll just do o(n)


class Solution(object):

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        total = [0]
        self.traverse(root, total)
        return total[0]

    def traverse(self, root, total):
        if not root:
            return
        total[0] += self.getTilt(root)
        self.traverse(root.left, total)
        self.traverse(root.right, total)

    def getSum(self, root, total):
        if not root:
            return
        total[0] += root.val
        self.getSum(root.left, total)
        self.getSum(root.right, total)

    def getTilt(self, root):
        left = [0]
        right = [0]
        self.getSum(root.left, left)
        self.getSum(root.right, right)
        return abs(left[0] - right[0])
