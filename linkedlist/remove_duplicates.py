"""remove duplicates functions"""

from linked_list import LinkedList


def remove_duplicates(linked_list: LinkedList) -> LinkedList:
    """removes duplicates using extra memory"""
    curr = linked_list.head

    # if empty linked list, there is nothing to remove
    if not curr:
        return linked_list
    # if there are values, try de-duplicating them with set
    s = []
    while curr:
        s.append(curr.data)
        curr = curr.next
    s = set(s)

    nll = LinkedList()
    for item in s:
        nll.append_to_tail(item)

    return nll


def remove_duplicates_no_extra_buffer(linked_list: LinkedList):
    """removes duplicates in memory"""
    curr = linked_list.head

    # if linkedlist-test is empty or has only one element
    if not curr or not curr.next:
        return
    while curr:
        if curr.next:
            # check if next is duplicate
            if curr.next.data == curr.data:
                curr.next = curr.next.next
            else:
                search = curr.next
                while search and search.next:
                    if search.next.data == curr.data:
                        search.next = search.next.next
                    search = search.next
        curr = curr.next


if __name__ == '__main__':
    ll = LinkedList("Mon")
    ll.append_to_tail("Tues")
    ll.append_to_tail("Wed")
    ll.append_to_tail("Mon")
    ll.append_to_tail("Thurs")
    ll.append_to_tail("Wed")
    ll.append_to_tail("Thurs")
    ll.append_to_tail("Fri")

    # nll = remove_duplicats(ll)
    # nll.print_list()
    remove_duplicates_no_extra_buffer(ll)
    ll.print_list()
