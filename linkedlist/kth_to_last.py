from linked_list import LinkedList, Node


def remove_kth_to_last(linked_list: LinkedList, k: int) -> Node:
    p1 = linked_list.head
    p2 = linked_list.head

    for i in range(0, k, 1):
        if not p1:
            return None
        p1 = p1.next

    while p1:
        p1 = p1.next
        p2 = p2.next

    return p2


if __name__ == '__main__':
    linked_list = LinkedList()
    for i in range(0, 5):
        linked_list.append_to_tail(i)
    node = remove_kth_to_last(linked_list, 5)
    print(node.data)
