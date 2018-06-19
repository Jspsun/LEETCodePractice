class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        A = [int(x) for x in a.replace('i','').split('+')]
        B = [int(x) for x in b.replace('i','').split('+')]
        return str(A[0]*B[0]-A[1]*B[1])+'+'+str(A[0]*B[1]+A[1]*B[0])+'i'
