class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        peopleDic = {}
        heights = []
        res = []

        for i in xrange(len(people)):
            p = people[i]
            if p[0] in peopleDic:
                peopleDic[p[0]].append((p[1], i))
            else:
                peopleDic[p[0]] = [(p[1],i)]
                heights.append(p[0])
        heights = sorted(heights, reverse = True)

        for h in heights:
            peopleDic[h].sort()
            for p in peopleDic[h]:
                res.insert(p[0], people[p[1]])
        return res

print Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
print Solution().reconstructQueue([])
