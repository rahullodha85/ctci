from linked_list import LinkedList, Node


def intersecting_node(list_a: LinkedList, list_b: LinkedList) -> Node:
    linked_list_set = set()

    head_a = list_a.head
    while head_a:
        linked_list_set.add(head_a)
        head_a = head_a.next

    head_b = list_b.head
    while head_b:
        if head_b in linked_list_set:
            return head_b
        head_b = head_b.next

    return None

def intersecting_node_alternative(list_a: LinkedList, list_b: LinkedList) -> Node:
    if not list_a.head or not list_b.head:
        return None

    len_a = 1
    len_b = 1

    head_a = list_a.head
    head_b = list_b.head

    while head_a:
        len_a += 1
        head_a = head_a.next

    while head_b:
        len_b += 1
        head_b = head_b.next

    # if tails are not the same, there is no intersection
    if head_a != head_b:
        return None

    diff = abs(len_a - len_b)

    head_a = list_a.head
    head_b = list_b.head

    if len_a > len_b:
        index = 0
        while index < diff:
            head_a = head_a.next
            index += 1

    else:
        index = 0
        while index < diff:
            head_b = head_b.next
            index += 1

    # now both lists are the same length
    while head_a and head_b:
        if head_a == head_b:
            return head_a
        head_a = head_a.next
        head_b = head_b.next

    return None

if __name__ == '__main__':
    # intersecting node example
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    linked_list_1.append_to_tail(1)
    linked_list_1.append_to_tail(2)
    linked_list_1.append_to_tail(3)

    linked_list_2.append_to_tail(4)
    linked_list_2.append_to_tail(5)

    # Creating an intersection
    linked_list_2.head.next.next = linked_list_1.head.next

    intersect_node = intersecting_node(linked_list_1, linked_list_2)
    print(f"Intersecting node: {intersect_node},  data: {intersect_node.data}")

    # Alternative method
    intersect_node_alt = intersecting_node_alternative(linked_list_1, linked_list_2)
    print(f"Intersecting node (alternative): {intersect_node_alt} data (alternative): {intersect_node_alt.data}")

    # No intersecting node example
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()
    linked_list_3.append_to_tail(1)
    linked_list_3.append_to_tail(2)
    linked_list_4.append_to_tail(3)

    intersect_node = intersecting_node(linked_list_3, linked_list_4)
    print(f"Intersecting node data: {intersect_node}")

    # Alternative method
    intersect_node_alt = intersecting_node_alternative(linked_list_3, linked_list_4)
    print(f"Intersecting node (alternative): {intersect_node_alt}")
