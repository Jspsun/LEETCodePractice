import math

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits = [0,1]
        for n in range (2, num+1):
            count = 0
            closestPower = int(math.floor(math.log(n,2)))
            if closestPower != 0:
                n-= 2**closestPower
                count +=1
            count += bits[n]
            bits.append(count)
        return bits[:num+1]

print (Solution().countBits(9))