class Solution(object):

    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        dic = {}
        sortedArray = sorted(nums, reverse=True)
        for i in range(len(sortedArray)):
            dic[sortedArray[i]] = i + 1
        for i in range(len(nums)):
            if (dic[nums[i]] == 1):
                nums[i] = "Gold Medal"
            elif(dic[nums[i]] == 2):
                nums[i] = "Silver Medal"
            elif(dic[nums[i]] == 3):
                nums[i] = "Bronze Medal"
            else:
                nums[i] = str(dic[nums[i]])
        return nums

s = Solution()
print s.findRelativeRanks([5, 4, 3, 2, 1])
