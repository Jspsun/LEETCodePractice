class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        excludeLastHouse = 0
        for n in nums:
            robbedLastHouse = i #temp to store the value of if you robbed the last house
            i = n + excludeLastHouse #rob this house
            excludeLastHouse = max(robbedLastHouse, excludeLastHouse) #update total to accomodat ehe best of exlidong or inclduging
        return max(i, excludeLastHouse)
