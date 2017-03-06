class Solution(object):

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        # could binary search too to get in logn time
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) / 2
            if target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return l

S = Solution()
print S.searchInsert([1, 3, 5, 6], 5)
