from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = Counter(s)
        ret = ""
        for l in sorted(m, key=m.get,reverse=True):
            ret += (l*m[l])
        return ret


print Solution().frequencySort("tree")
