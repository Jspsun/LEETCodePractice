class Solution(object):
    #brute force o(n^2)
    # def dailyTemperatures(self, temperatures):
    #     """
    #     :type temperatures: List[int]
    #     :rtype: List[int]
    #     """
    #     ret = []
    #     for i in xrange(len(temperatures)):
    #         for j in xrange (i+1, len(temperatures)):
    #             if temperatures[j] > temperatures[i]:
    #                 ret.append(j-i)
    #                 break
    #             if j==len(temperatures)-1:
    #                 ret.append(0)
    #                 break
    #     ret.append(0)
    #     return ret

    #o(n)
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        s = []
        ret =[0 for i in xrange(len(temperatures))]
        for i in xrange(len(temperatures)):
            while len(s)>0 and temperatures[i]>temperatures[s[-1]]:
                inx=s.pop()
                ret[inx]=i-inx
            s.append(i)
        return ret
print Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])


