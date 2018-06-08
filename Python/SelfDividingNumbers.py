class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isMagic(n):
            for d in str(n):
                if d =='0' or n%int(d)!=0:
                    return False
            return True

        l=[]
        for n in range(left, right+1):
            if isMagic(n):
                l.append(n)
        return l
