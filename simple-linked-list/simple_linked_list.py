class Node(object):
    def __init__(self, value, next=None):
        self.__value, self.__next = value, next

    def next(self):
        return self.__next

    def value(self):
        return self.__value


class LinkedList(object):
    def __init__(self, values=[]):
        self.__head, self.__length = None, 0
        for item in values:
            self.push(item)

    def __len__(self):
        return self.__length

    def __iter__(self):
        node = self.__head
        while node:
            yield node.value()
            node = node.next()

    def reversed(self):
        return LinkedList(list(self))

    def head(self):
        if not self.__head:
            raise EmptyListException("Empty")
        return self.__head

    def push(self, value):
        if not self.__head:
            self.__head = Node(value)
        else:
            self.__head = Node(value, self.__head)
        self.__length += 1

    def pop(self):
        if not self.__head:
            raise EmptyListException("Empty")
        node = self.__head
        self.__head = node.next()
        self.__length -= 1
        return node.value()


class EmptyListException(Exception):
    pass
