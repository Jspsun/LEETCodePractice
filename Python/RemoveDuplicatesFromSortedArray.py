class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for n in nums:
            s.add(n)
        nums = list(s)
        return nums

S = Solution()
print S.removeDuplicates([1, 1, 2])
