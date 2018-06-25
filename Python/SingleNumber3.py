class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set([])
        for n in nums:
            if n in s:
                s.discard(n)
            else:
                s.add(n)
        return list(s)
