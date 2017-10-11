class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <3:
            return 0

        dp =[0 for i in xrange(len(A))]
        if A[1]-A[0] == A[2]-A[1]:
            dp[2]=1

        for i in range (3,len(A)):
            if A[i]-A[i-1]== A[i-1]-A[i-2]:
                dp[i]= 1 +dp[i-1]
        return sum(dp)
            