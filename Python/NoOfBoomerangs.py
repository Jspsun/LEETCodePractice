class Solution(object):

    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        total = 0

        for p in points:
            dic = {}
            for q in points:
                if p == q:
                    continue
                x = p[0] - q[0]
                y = p[1] - q[1]
                dic[x * x + y * y] = 1 + dic.get(x * x + y * y, 0)
            for m in dic:
                total += dic[m] * (dic[m] - 1)
        return total

S = Solution()
print S.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]])
