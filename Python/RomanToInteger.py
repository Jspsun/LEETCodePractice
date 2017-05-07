class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        t = 0
        for i in range(len(s) - 1):
            if m[s[i]] < m[s[i + 1]]:
                t -= m[s[i]]
            else:
                t += m[s[i]]
        return t + m[s[-1]]

print Solution().romanToInt("DCXXI")
