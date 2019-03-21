class Node(object):
    def __init__(self, value, succeeding=None, previous=None):
        self.value, self.succeeding, self.previous = value, succeeding, previous

    def next(self):
        return self.succeeding


class LinkedList(object):
    def __init__(self, values=[]):
        self.root, self.length = Node(None), 0
        self.root.previous = self.root.succeeding = self.root
        for item in values:
            self.push(item)

    def __len__(self):
        return self.length

    def __iter__(self):
        node = self.root.succeeding
        while node.value:
            node = node.succeeding
            yield node.previous.value

    def reversed(self):
        return self.__iter__()

    def _link(self, value, previous):
        node = Node(value, previous.succeeding, previous)
        node.previous.succeeding = node
        node.succeeding.previous = node

    def _unlink(self, node):
        node.previous.succeeding = node.succeeding
        node.succeeding.previous = node.previous
        return node.value

    def head(self):
        return self.root

    def push(self, value):
        self._link(value, self.root.previous)
        self.length += 1

    def pop(self):
        self.length -= 1
        if not self.length:
            raise EmptyListException("List is empty.")
        return self._unlink(self.root.previous)


class EmptyListException(Exception):
    pass
