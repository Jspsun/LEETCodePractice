class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s =  set([])
        count = 0
        for w in words:
            m = ""
            for l in w:
                m+=morse[ord(l)-ord("a")]
            if m not in s:
                count +=1
                s.add(m)
        return count

print Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
