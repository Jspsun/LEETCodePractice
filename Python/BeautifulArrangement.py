class Solution(object):
    counter = 0
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.counter = 0
        m = {}
        for i in xrange(1, N+1):
            m[i]=[]
            for n in xrange(1, N+1):
                if n%i==0 or i%n==0:
                    m[i].append(n)
        self.bfs(N, set([]), m)
        return self.counter
    
    def bfs(self, position, cache, m):
        if position <=0:
            self.counter+=1
            return
        for number in m[position]:
            if number not in cache:
                s = set(cache)
                s.add(number)
                self.bfs(position-1, s, m)
        
print Solution().countArrangement(2)
