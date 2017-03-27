class Solution(object):

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # same as word pattern question.
        return map(s.find, s) == map(t.find, t)
