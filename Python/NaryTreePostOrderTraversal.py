"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # self.path = []
        # def dfs(root):
        #     if not root:
        #         return
        #     for c in root.children:
        #         dfs(c)
        #     self.path.append(root.val)
        # dfs(root)
        # return self.path
        s = [root]
        path = []
        while len(s) > 0:
            n = s.pop()
            if n:
                path.insert(0, n.val)
                for c in n.children:
                    s.append(c)
        return path


