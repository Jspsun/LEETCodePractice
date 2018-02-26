class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        p1 = 0
        p2 = 0
        while p2 < len(chars):
            temp=chars[p2]
            counter = 0
            while p2 < len(chars) and chars[p2] == temp:
                p2+=1
                counter +=1
            newStr=temp+str(counter)
            if counter == 1:
                newStr = temp
            chars[p1:p1+len(newStr)]=newStr
            p1+=len(newStr)
        return p1

S=Solution()
print S.compress(["a","a","b"])
