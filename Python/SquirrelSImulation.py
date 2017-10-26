class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        sum = 0
        for n in nuts:
            sum += 2*self.transport(n, tree)
        return min([sum - self.transport(n, tree) + self.transport(n, squirrel) for n in nuts])
    
    def transport(self, nut, tree):
        return abs(nut[0]-tree[0]) + abs(nut[1]-tree[1])



