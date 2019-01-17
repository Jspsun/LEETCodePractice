"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        self.max_depth = 0;
        def dfs(root, depth):
            if not root:
                return
            self.max_depth = max(depth, self.max_depth)
            for c in root.children:
                dfs(c, depth + 1)
        dfs(root, 1)
        return self.max_depth


