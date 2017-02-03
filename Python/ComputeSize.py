def computeSize(root):
    dict = {}
    helper(dict, root)
    return dict


def helper(dict, root):

    if root.left == None and root.right == None:
        dict[root] = 1
        return

    helper(dict, root.left)
    helper(dict, root.right)

    dict[root] = dict[root.left] + dict[root.right] + 1

from TestObjects import *

b = BinaryTree()
dict = computeSize(b.root)
for e in dict:
    print e.val, dict[e]
