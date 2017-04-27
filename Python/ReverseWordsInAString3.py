class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([t[::-1]for t in s.split()])

S=Solution()
print S.reverseWords("Let's take LeetCode contest")