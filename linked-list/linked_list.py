class Node(object):
    def __init__(self, value, succeeding=None, previous=None):
        self.value, self.succeeding, self.previous = value, succeeding, previous


class LinkedList(object):
    def __init__(self):
        self.root, self.length = Node(None), 0
        self.root.previous = self.root.succeeding = self.root

    def __len__(self):
        return self.length

    def __iter__(self):
        node = self.root.succeeding
        while node.value:
            node = node.succeeding
            yield node.previous.value

    def _link(self, value, previous):
        node = Node(value, previous.succeeding, previous)
        node.previous.succeeding = node
        node.succeeding.previous = node

    def _unlink(self, node):
        node.previous.succeeding = node.succeeding
        node.succeeding.previous = node.previous
        return node.value

    def push(self, value):
        self._link(value, self.root.previous)
        self.length += 1

    def pop(self):
        self.length -= 1
        return self._unlink(self.root.previous)

    def shift(self):
        self.length -= 1
        return self._unlink(self.root.succeeding)

    def unshift(self, value):
        self._link(value, self.root)
        self.length += 1
