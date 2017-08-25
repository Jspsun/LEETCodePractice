# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans = []
        self.dfs(ans, 1, root)
        ans = map(lambda l: sum(l) * 1.0 / len(l), ans)
        return ans

    def dfs(self, ans, depth, node):
        if not node:
            return
        if len(ans) < depth:
            ans.append([node.val])
        else:
            ans[depth-1].append(node.val)
        self.dfs(ans, depth + 1, node.left)
        self.dfs(ans, depth + 1, node.right)
