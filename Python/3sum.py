class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(len(nums)):
            ret = self.twoSum( nums[:i]+nums[i+1:] , 0-nums[i])
            if ret:
                temp = sorted([nums[i]] + ret)
                if temp not in ans:
                    ans.append(temp)
        return ans


    
    def twoSum(self, nums, k):
        s = set([])
        for n in nums:
            if k-n in s:
                return [k-n, n]
            s.add(n)
        return False
