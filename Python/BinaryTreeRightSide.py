# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # right side of each level
        list = []
        self.bfs(root, list, 0)
        return list

    def bfs(self, root, list, level):
        if not root:
            return
        if len(list) <= level:
            list.append(root.val)

        self.bfs(root.right, list, level + 1)
        self.bfs(root.left, list, level + 1)


from TestObjects import *
b = BinaryTree()
s = Solution()
print s.rightSideView(b.root)
