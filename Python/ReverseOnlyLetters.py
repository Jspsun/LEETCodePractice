class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        i = 0
        j = len(S) - 1

        S = list(S)
        while i < j:
            while i < j and not S[j].isalpha():
                j -=1
            while i < j and not S[i].isalpha():
                i +=1
            S[i] , S[j] = S[j], S[i]
            i, j = i + 1, j - 1
        return "".join(S)




print Solution().reverseOnlyLetters("ab-cd")