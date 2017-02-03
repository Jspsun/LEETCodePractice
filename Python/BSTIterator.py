# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.list = deque()
        self.inOrderTraversal(root, self.list)

    def inOrderTraversal(self, root, list):
        if root == None:
            return
        self.inOrderTraversal(root.left, list)
        list.append(root.val)
        self.inOrderTraversal(root.right, list)

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.list) > 0:
            return True
        return False

    def next(self):
        """
        :rtype: int
        """
        return self.list.popleft()


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
