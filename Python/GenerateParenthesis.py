class Solution(object):
    list = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.list = []
        self.helper(n, "", 0, 0)
        return self.list

    def helper(self, n, string, left, right):
        if len(string) == n * 2:
            self.list.append(string)
            return
        if left <= n and left < n:
            self.helper(n, string + '(', left + 1, right)
        if left > right:
            self.helper(n, string + ')', left, right + 1)

print Solution().generateParenthesis(2)
