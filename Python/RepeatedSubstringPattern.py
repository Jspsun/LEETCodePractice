class Solution(object):

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        text = ""
        for c in s:
            text += c
            if len(text) > l / 2:
                return False

            if text * (l / len(text)) == s:
                return True
