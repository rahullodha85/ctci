"""delete first occurrence function"""

from linked_list import LinkedList


def delete_first_occurrence(ll: LinkedList, data: int) -> None:
    """deletes first occurrence of node with matching data"""
    curr = ll.head

    # return if empty linked list
    if not curr:
        return

        # iterate till first matching node is found
    while curr:
        # if matching node found, remove this node
        if curr.data == data:
            next_node = curr.next
            curr.data = next_node.data
            curr.next = next_node.next
            return

        curr = curr.next


if __name__ == '__main__':
    linked_list = LinkedList()
    for i in range(0, 5):
        linked_list.append_to_tail(i)
    linked_list.append_to_tail(2)
    linked_list.print_list()
    delete_first_occurrence(linked_list, 2)
    linked_list.print_list()
