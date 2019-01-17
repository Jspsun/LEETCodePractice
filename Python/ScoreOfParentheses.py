class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        memo = []
        for l in S:
            if l == ')':
                memo.pop()
            else:
                memo.append(l)
