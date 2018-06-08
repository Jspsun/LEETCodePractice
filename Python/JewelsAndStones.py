class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jset = set(J)
        count = 0
        for l in S:
            if l in jset:
                count+=1
        return count

print Solution().numJewelsInStones("aA", "aAAbbbb")
