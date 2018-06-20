class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        def recurse(room):
            if room in visited:
                return
            visited.add(room)
            for k in rooms[room]:
                recurse(k)

        visited = set([])
        recurse(0)
        return len(visited) == len(rooms)

print Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]])
