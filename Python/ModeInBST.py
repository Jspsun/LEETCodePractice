# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []

        dic = {}
        self.helper(root, dic)
        highest = max(dic.values())
        list = []
        for e in dic:
            if dic[e] == highest:
                list.append(e)
        return list

    def helper(self, root, dic):
        if root:
            dic[root.val] = dic.get(root.val, 0) + 1
            self.helper(root.left, dic)
            self.helper(root.right, dic)
