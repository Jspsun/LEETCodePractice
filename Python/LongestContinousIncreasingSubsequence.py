class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0

        largest = 1
        current = 1
        for n in xrange(len(nums)):
            if n-1 >= 0 and nums[n-1] < nums[n]:
                current +=1
                largest =max(current, largest)
            else:
                current = 1
        return largest

S = Solution()
print S.findLengthOfLCIS([1,3,5,4,7])==3
print S.findLengthOfLCIS([1])==1
print S.findLengthOfLCIS([2,1])==1
print S.findLengthOfLCIS([2,1,2])==2
