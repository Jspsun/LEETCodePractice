class Solution(object):

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        r = []
        pMap = {}
        cMap = {}
        for i in range(0, len(p)):
            cMap[s[i]] = cMap.get(s[i], 0) + 1
        for n in p:
            pMap[n] = pMap.get(n, 0) + 1

        if cMap == pMap:
            r.append(0)
        for i in range(0, len(s) - len(p)):
            cMap[s[i]] -= 1
            if cMap[s[i]] == 0:
                del cMap[s[i]]
            cMap[s[i + len(p)]] = cMap.get(s[i + len(p)], 0) + 1
            if cMap == pMap:
                r.append(i + 1)
        return r

print Solution().findAnagrams("cbaebabacd", "abc")
