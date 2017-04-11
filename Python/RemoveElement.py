class Solution(object):

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        dex = 0
        while dex < len(nums):
            if nums[dex] == val:
                nums = nums[:dex] + nums[dex + 1:]
                dex -= 1
            dex += 1

        return len(nums)

S = Solution()
print S.removeElement([3, 2, 2, 3], 3)
