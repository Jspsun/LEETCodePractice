# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    # main that gets weights and dfs through the tree
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        if root == None:
            return 0
        values = {}
        self.precompute(root, 0, values)

        # for e in values:
        #     print e.val, values[e]

        matches = [0]
        # iterate through all nodes
        s = []
        s.append(root)
        while len(s) > 0:
            x = s.pop()
            self.getMatches(x, x, values, matches, sum)
            if x.right:
                s.append(x.right)
            if x.left:
                s.append(x.left)
        return matches[0]

    # compute the weight of the current subtree
    # computes weight from root
    def precompute(self, root, upper, values):
        if not root:
            return
        values[root] = root.val + upper
        self.precompute(root.left, values[root], values)
        self.precompute(root.right, values[root], values)

    # dfs from given root and checks for any sum matches
    def getMatches(self, root, current, values, matches, sum):
        if not current:
            return

        if values[current] + root.val - values[root] == sum:
            matches[0] += 1
            # print current.val, root.val
        self.getMatches(root, current.left, values, matches, sum)
        self.getMatches(root, current.right, values, matches, sum)
