class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                r += 1
                l -= 1
            return r - l - 1

        start = 0
        end = 0
        for i in range(len(s)):
            trial1 = expand(s, i, i)
            trial2 = expand(s, i, i + 1)
            best = max(trial1, trial2)
            if best > end - start:
                start = i - (best - 1) / 2
                end = i + best / 2
        return s[start:end+1]

print Solution().longestPalindrome("abcda")