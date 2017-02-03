# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        master = []
        list = []
        self.traverse(root, list, master)
        return master

    def traverse(self, root, list, master):
        if not root:
            return
        list.append(str(root.val))
        if root.left == None and root.right == None:
            master.append("->".join(list))
            return

        self.traverse(root.left, list[:], master)
        self.traverse(root.right, list[:], master)


from TestObjects import *
b = BinarySearchTree()
s = Solution()
print s.binaryTreePaths(None)
