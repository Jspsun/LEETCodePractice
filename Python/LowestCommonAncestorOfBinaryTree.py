# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # load up hashmap for parents
        map = {}
        self.load(root, map)
        pAncestors = set([p])
        while p != root:
            p = map[p]
            pAncestors.add(p)
        if q in pAncestors:
            return q
        while q != root:
            q = map[q]
            if q in pAncestors:
                return q

    def load(self, root, map):
        if not root:
            return
        if root.left:
            map[root.left] = root
        if root.right:
            map[root.right] = root
        self.load(root.left, map)
        self.load(root.right, map)
