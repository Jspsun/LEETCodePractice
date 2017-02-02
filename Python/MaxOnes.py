class Solution(object):

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = 0
        temp = 0
        for n in nums:
            if n == 1:
                temp += 1
                largest = max(temp, largest)
            else:
                temp = 0
        return largest
    print findMaxConsecutiveOnes(object, [1])
