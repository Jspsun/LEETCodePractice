class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        dp = [1 for i in xrange(len(pairs))]
        pairs=sorted(pairs, key = lambda p:p[1])
        current = -9999
        longest = 0
        for p in pairs:
            if current < p[0]:
                current =  p[1]
                longest +=1
        return longest