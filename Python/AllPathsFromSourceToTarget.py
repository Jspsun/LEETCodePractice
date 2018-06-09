class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        def dfs(node,path):
            if node == len(graph)-1:
                ret.append(path)
                return
            if graph[node]==[]:
                return
            for n in graph[node]:
                dfs(n, path+[n])
        dfs(0, [0])
        return ret
