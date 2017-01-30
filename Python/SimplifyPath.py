class Solution(object):

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        tokens = path.split("/")

        path = []

        for t in tokens:
            if t == '..' and len(path) > 0:
                path.pop()
            elif t != '.' and t != '' and t != '..':
                path.append(t)

        # print path
        if path == [""] or path == []:
            return '/'

        path.insert(0, "")

        return "/".join(path)

s = Solution()
print s.simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///")
