"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        memo = []

        def dfs(root, depth):
            if not root:
                return
            if len(memo)-1 < depth:
                memo.append([])
            memo[depth].append(root.val)
            for child in root.children:
                dfs(child, depth + 1)

        dfs(root, 0)
        return memo

