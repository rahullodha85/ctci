from linkedlist.linked_list import LinkedList


def sum_list(list_a: LinkedList, list_b: LinkedList):
    curr_a = list_a.head
    curr_b = list_b.head

    result_list = LinkedList()
    carry_over = 0
    while curr_a and curr_b:
        sum_val = curr_a.data + curr_b.data + carry_over
        carry_over = 0
        if sum_val > 10:
            sum_val = sum_val%10
            carry_over = 1
        result_list.append_to_tail(sum_val)

        curr_a = curr_a.next
        curr_b = curr_b.next

    if curr_a:
        while curr_a:
            if carry_over > 0:
                result_list.append_to_tail(curr_a.data + carry_over)
                carry_over = 0
            else:
                result_list.append_to_tail(curr_a.data)
            curr_a = curr_a.next

    if curr_b:
        while curr_b:
            if carry_over > 0:
                result_list.append_to_tail(curr_b.data + carry_over)
                carry_over = 0
            else:
                result_list.append_to_tail(curr_b.data)
            curr_b = curr_b.next

    return result_list


if __name__ == '__main__':
    linked_list_1 = LinkedList()
    linked_list_1.append_to_tail(7)
    linked_list_1.append_to_tail(1)
    linked_list_1.append_to_tail(6)

    linked_list_2 = LinkedList()
    linked_list_2.append_to_tail(5)
    linked_list_2.append_to_tail(9)
    linked_list_2.append_to_tail(2)

    result_list = sum_list(linked_list_1, linked_list_2)
    result_list.print_list()
