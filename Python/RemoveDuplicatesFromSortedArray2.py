class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for n in nums:
            #checking if current num is > than the 2 before it
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i