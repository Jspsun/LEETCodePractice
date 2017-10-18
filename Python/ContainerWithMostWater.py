class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height)-1
        best = 0

        while start < end:
            best = max(best, self.getArea(start,end,height))
            if height[start] < height[end]:
                start +=1
            else:
                end-=1
        return best

    def getArea (self, start, end, height):
        return min(height[start], height[end]) * (end - start)

