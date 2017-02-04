class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        self.front = None

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if not self.s1:
            self.front = x
        self.s1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.s2:
            return self.front
        return self.s2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.s1 and not self.s2


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
# print obj.pop()
# print obj.pop()

print obj.peek()
print obj.peek()


# print obj.empty()
