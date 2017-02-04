class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.min = 9999999999

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x <= self.min:
            self.s.append(self.min)
            self.min = x
        self.s.append(x)

    def pop(self):
        """
        :rtype: void
        """
        temp = self.s.pop()
        if temp == self.min:
            self.min = self.s.pop()
        return temp

    def top(self):
        """
        :rtype: int
        """
        if not self.s:
            return None
        return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
