class Solution(object):
    def optimalDivision(self, A):
        A = map(str, A)
        if len(A) <= 2: return '/'.join(A)
        return '{}/({})'.format(A[0], '/'.join(A[1:]))

print Solution().optimalDivision([1000,100,10,2])=="1000/(100/10/2)"

