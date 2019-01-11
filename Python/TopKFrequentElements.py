from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c = Counter(nums)
        m = {}
        for n in c:
            m[c[n]]= m.get(c[n],[])+[n]

        for n in sorted(m):
            for e in m[n]


print Solution().topKFrequent([1,1,1,2,2,2,3], 2)
