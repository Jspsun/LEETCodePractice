class Solution(object):
    def peakIndexInMountainArray(self, A):
        lo = 0
        hi = len(A) - 1
        while lo < hi:
            mi = (lo + hi) / 2
            if A[mi] < A[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo
