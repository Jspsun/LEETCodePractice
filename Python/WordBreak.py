class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for i in xrange(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for w in wordDict:
                if len(w)<= i and dp[i-len(w)]:
                    if s[i-len(w):i]==w:
                        dp[i] = True
                        break
        return dp[-1]

print Solution().wordBreak("leetcode", ["leet","code"])==True
print Solution().wordBreak("leetcode", ["wowwwww","caode"])==False
print Solution().wordBreak("aaaaaaa", ["aaaa","aa"])==False