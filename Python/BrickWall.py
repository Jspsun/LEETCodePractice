class Solution(object):

    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        # hashmap for each width
        # iterate through each and add

        width = sum(wall[0])
        m = {}
        for r in wall:
            total = 0
            for c in r:
                total += c
                if total != width:
                    m[total] = m.get(total, 0) + 1
        max = 0
        print m
        for e in m:
            if m[e] > max:
                max = m[e]
        return len(wall) - max

print Solution().leastBricks([[7, 1, 2], [3, 5, 1, 1], [10]])
