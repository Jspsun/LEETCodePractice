
class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        shortest = min(strs, key=len)
        for i in range(len(shortest), 0 - 1, -1):
            isPrefix = True
            for s in strs:
                if s[0:i] != shortest[0:i]:
                    isPrefix = False
                    break
            if isPrefix:
                return shortest[0:i]

        # return ""

S = Solution()
print "|" + S.longestCommonPrefix([]) + "|"

# can do with indexOf(pre)!=0
# remove last letter from pre each time
# iterate
