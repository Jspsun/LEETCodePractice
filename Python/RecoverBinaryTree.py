# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def __init__(self):
        self.firstElement = None
        self.prevElement = None
        self.prevElement = TreeNode(-9999999)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.traverse(root)
        temp = self.firstElement.val
        self.firstElement.val = self.secondElement.val
        self.secondElement.val = temp

    def traverse(self, root):
        if not root:
            return

        # preorder traverse
        self.traverse(root.left)

        # if first element has not been found, assign it to prev element (as
        # long as the prev > currentNode)
        if not self.firstElement and self.prevElement.val >= root.val:
            self.firstElement = self.prevElement

        # if first element is found assign second element to the root
        if self.firstElement and self.prevElement.val >= root.val:
            self.secondElement = root

        self.prevElement = root

        self.traverse(root.right)
