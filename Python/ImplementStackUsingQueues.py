class MyStack(object):

    # did it with a single queue
    def __init__(self):
        self._queue = collections.deque()

    # stores everything as if it were a stack
    def push(self, x):
        q = self._queue
        q.append(x)
        for i in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self):
        return self._queue.popleft()

    def top(self):
        return self._queue[0]

    def empty(self):
        return not len(self._queue)
