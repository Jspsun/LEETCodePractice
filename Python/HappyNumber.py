class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = n
        fast = n
        while True:
            slow = self.digitSquareSum(slow)
            fast = self.digitSquareSum(fast)
            fast = self.digitSquareSum(fast)

            if slow == fast:
                break
        if slow == 1:
            return True
        return False

    def digitSquareSum(self, n):
        temp = 0
        while n != 0:
            temp += (n % 10) * (n % 10)
            n /= 10
        return temp

S = Solution()
print S.isHappy(1)
