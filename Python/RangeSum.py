class NumArray(object):

    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.memo = []
        if len(nums) > 0:
            self.memo = [nums[0]]
            for i in range(1, len(nums)):
                self.memo.append(self.memo[-1] + nums[i])
            self.nums = nums

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.memo == []:
            return 0
        return self.memo[j] - self.memo[i] + (self.nums[i])


# Your NumArray object will be instantiated and called as such:
numArray = NumArray([-2, 0, 3, -5, 2, -1])
print numArray.sumRange(0, 2)  # 1
print numArray.sumRange(2, 5)  # -1
print numArray.sumRange(0, 5)  # -3
