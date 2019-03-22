import collections


class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self.buffer = collections.deque()
        self.CAPACITY = capacity

    def read(self):
        if not len(self.buffer):
            raise BufferEmptyException("Cannot read from an empty buffer.")
        return self.buffer.popleft()

    def write(self, data):
        if len(self.buffer) == self.CAPACITY:
            raise BufferFullException("Cannot write to a buffer that is at capacity.")
        self.buffer.append(data)

    def overwrite(self, data):
        if len(self.buffer) == self.CAPACITY:
            self.buffer.popleft()
        self.write(data)

    def clear(self):
        self.buffer = collections.deque()
