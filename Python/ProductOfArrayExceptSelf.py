class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def multiply(a, b):
            return a*b

        # multiply left to right both sides
        ls=[1]
        for i in xrange(1, len(nums)):
            ls.append(ls[-1]*nums[i-1])
        rs=[1]
        for i in xrange(len(nums)-1,0,-1):
            rs.insert(0, rs[0]*nums[i])
        return map(multiply, ls, rs)


print(Solution().productExceptSelf([1,2,3,4]))

# [1,1,2,6]
# [24,12,4,1]
