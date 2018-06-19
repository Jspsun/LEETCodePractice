class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        m={}
        for i in xrange(len(S)):
            m[S[i]]=i
        #filter letters
        f=""
        return ''.join(sorted(T, key=m.get))


print Solution().customSortString("cba", "abcd")
