class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        vertical = 0
        horizontal = 0
        for m in moves:
            if m == 'U':
                vertical +=1
            elif m == 'D':
                vertical -=1
            elif m == 'R':
                horizontal +=1
            else:
                horizontal -=1
        return vertical == 0 and horizontal == 0
        
