class Solution(object):

    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # check for even index number to see when it is off by one in terms of
        # pairs. ex. if an even index number is followed by a differnt number,
        # the extra number is to the left of the checked index
        n = len(nums)
        l = 0
        h = n / 2
        while l < h:
            m = (l + h) / 2
            if nums[2 * m] != nums[2 * m + 1]:
                h = m
            else:
                l = m + 1
        return nums[2 * l]
