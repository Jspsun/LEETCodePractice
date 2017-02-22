class Solution(object):

    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # kids
        g.sort()

        # cookies
        s.sort()

        kidDex = 0
        cookieDex = 0
        while kidDex < len(g) and cookieDex < len(s):
            if s[cookieDex] >= g[kidDex]:
                kidDex += 1
            cookieDex += 1
        return kidDex
