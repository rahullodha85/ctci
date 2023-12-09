from linked_list import LinkedList


def remove_duplicats(ll: LinkedList) -> LinkedList:
    curr = ll.head

    # if empty linked list, there is nothing to remove
    if not curr:
        return ll
    # if there are values, try de-duplicating them with set
    else:
        s = []
        while curr:
            s.append(curr.data)
            curr = curr.next
        s = set(s)

    nll = LinkedList()
    for item in s:
        nll.append_to_tail(item)

    return nll


def remove_duplicates_no_extra_buffer(ll: LinkedList):
    curr = ll.head

    # if linked-list is empty or has only one element
    if not curr or not curr.next:
        return
    else:
        while curr:
            if curr.next:
                search = curr.next
                while search:

                    search = search.next

            curr = curr.next



if __name__ == '__main__':
    ll = LinkedList("Mon")
    ll.append_to_tail("Tues")
    ll.append_to_tail("Wed")
    ll.append_to_tail("Mon")
    ll.append_to_tail("Thurs")

    nll = remove_duplicats(ll)
    nll.print_list()
