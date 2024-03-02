class Node:  # pylint: disable=too-few-public-methods
    """Node class with data and next"""

    def __init__(self, data):
        """default constructor that initializes a node"""
        self.data = data
        self.next = None


class Stack:
    def __init__(self, data=None):
        if not data:
            self.top = None
        else:
            node = Node(data)
            self.top = node

    def is_empty(self):
        return self.top is None

    def peek(self):
        if not self.is_empty():
            return self.top.data
        return None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty")

        data = self.top.data
        self.top = self.top.next
        return data
