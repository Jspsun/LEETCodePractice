class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        def merge(intervals):
            """
            :type intervals: List[Interval]
            :rtype: List[Interval]
            """
            new_intervals = []

            num = len(intervals)
            intervals.sort()
            i = 0
            while i < num:
                s = intervals[i][0]
                e = intervals[i][1]
                j = i + 1
                while j < num and e >= intervals[j][0]:
                    e = max(e, intervals[j][1])
                    j += 1
                new_intervals.append([s, e])
                i = j

            return new_intervals
        m={}
        for i in xrange(len(S)):
            if  S[i] not in m:
                m[S[i]]=[i,i]
            else:
                m[S[i]][1]=i
        intervals = merge([m[n] for n in m])
        return [i[1]+1-i[0] for i in intervals]


print Solution().partitionLabels("ababcbacadefegdehijhklij")
