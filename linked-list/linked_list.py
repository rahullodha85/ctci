class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data=None):
        if not data:
            self.head = None
        else:
            node = Node(data)
            self.head = node

    def append_to_tail(self, data):
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
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def insert_at_begin(self, data):
        node = Node(data)

        # if linked list is empty, make new node head of linked list
        if not self.head:
            self.head = node
        else:
            temp = self.head
            self.head = node
            node.next = temp

    def insert_at_index(self, index: int, data):
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
                raise Exception(f"index: {index} is not present in linked list")

    def delete_node(self, data):
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

    def delete_at_index(self):
        pass


if __name__ == '__main__':
    ll = LinkedList(5)
    ll.append_to_tail(4)
    ll.append_to_tail(3)
    ll.append_to_tail(7)
    ll.insert_at_begin(1)
    ll.insert_at_index(0, 2)
    # ll.delete_node(7)
    ll.print_list()
