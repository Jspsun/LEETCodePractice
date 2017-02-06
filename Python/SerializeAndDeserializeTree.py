# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        data = []

        def preOrder(root):
            if not root:
                data.append('#')
                return
            data.append(str(root.val))
            preOrder(root.left)
            preOrder(root.right)
        preOrder(root)
        return ','.join(data)

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def construct():
            current = data.pop(0)
            if current == '#':
                return None
            root = TreeNode(int(current))
            root.left = construct()
            root.right = construct()
            return root
        data = data.split(',')
        return construct()
