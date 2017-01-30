# Test objects used to test code
# I made a few sample preloaded data structures to test the basic
# functionality of some of my solutions


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinarySearchTree(object):

    def __init__(self):
        self.root = TreeNode(6)
        self.root.left = TreeNode(2)
        self.root.left.left = TreeNode(0)
        self.root.left.right = TreeNode(4)
        self.root.left.right.left = TreeNode(3)
        self.root.left.right.right = TreeNode(5)
        self.root.right = TreeNode(8)
        self.root.right.left = TreeNode(7)
        self.root.right.right = TreeNode(9)
