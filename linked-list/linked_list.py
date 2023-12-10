"""linked list and node classes"""


class Node:  # pylint: disable=too-few-public-methods
    """Node class with data and next"""

    def __init__(self, data):
        """default constructor that initializes a node"""
        self.data = data
        self.next = None


class LinkedList:
    """linked list class"""

    def __init__(self, data=None):
        """default constructor that initializes an empty or single node linked list"""
        if not data:
            self.head = None
        else:
            node = Node(data)
            self.head = node

    def append_to_tail(self, data):
        """appends a node at the end of liinked list"""
        end = Node(data)

        # if linked list is empty, make new node the head
        if not self.head:
            self.head = end
            return

        # if not empty
        curr = self.head

        # traverse to end of linked list and add new node
        while curr.next:
            curr = curr.next
        curr.next = end

    def print_list(self):
        """prints whole linked list"""
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def insert_at_begin(self, data):
        """inserts node at the beginning"""
        node = Node(data)

        # if linked list is empty, make new node head of linked list
        if not self.head:
            self.head = node
        else:
            temp = self.head
            self.head = node
            node.next = temp

    def insert_at_index(self, index: int, data):
        """inserts node at index"""
        node = Node(data)

        # if linked list is empty or index is 0 insert at beginning
        if not self.head and index == 0:
            self.insert_at_begin(data)
        else:
            # non empty linked list index 0 insertion
            if index == 0:
                self.insert_at_begin(data)
                return
            position = 0
            curr = self.head
            while curr:
                if index == position + 1:
                    node.next = curr.next
                    curr.next = node
                position += 1
                curr = curr.next
            if index >= position:
                raise IndexError(f"index: {index} is not present in linked list")

    def delete_node(self, data):
        """deletes first node that matches data"""
        curr = self.head

        # if head is to be removed
        if curr and curr.data == data:
            self.head = curr.next
            curr = None
            return

        # if head is not to be removed
        while curr and curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
            curr = curr.next

        # if last node is to be removed
        if curr:
            curr = None

    def delete_at_index(self, index: int):
        """deletes node at index"""
        # if linked list is empty, deletion not possible
        if not self.head:
            raise IndexError('linked list is empty')
        curr = self.head
        position = 0
        while curr:
            if index == position + 1:
                if curr.next:
                    curr.next = curr.next.next
                # deletion at the end
                else:
                    curr.next = None
            position += 1
            curr = curr.next
        if index > position:
            raise IndexError(f"index: {index} is not present in linked list")


if __name__ == '__main__':
    ll = LinkedList(5)
    ll.append_to_tail(4)
    ll.append_to_tail(3)
    ll.append_to_tail(7)
    ll.insert_at_begin(1)
    # ll.insert_at_index(0, 2)
    # ll.delete_node(7)
    ll.delete_at_index(4)
    ll.print_list()
