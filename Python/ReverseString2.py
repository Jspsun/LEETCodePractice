class Solution(object):

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # tokenize into groups of 2k
        # reverse the first k
        # join
        tokens = []
        for i in range(0, len(s), 2 * k):
            tokens.append(s[i:i + 2 * k])
        r = ''
        for t in tokens:
            r += t[:k][::-1] + t[k:]
        return r

print Solution().reverseStr("abcdefg", 1)
