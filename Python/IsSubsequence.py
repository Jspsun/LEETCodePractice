from collections import deque


class Solution(object):

    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = deque(s)
        for l in t:
            if len(s) == 0:
                return True
            if l == s[0]:
                s.popleft()
        return len(s) == 0

print Solution().isSubsequence("abc", "ahbgdc")
