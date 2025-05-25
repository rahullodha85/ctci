from linked_list import LinkedList, Node

def detect_loop(head: Node) -> bool:
    """
    Detects if a loop exists in the linked list using Floyd's Cycle Detection Algorithm (Tortoise and Hare).
    :param head: The head of the linked list.
    :return: True if a loop exists, False otherwise.
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

if __name__ == "__main__":
    # Example usage
    ll = LinkedList()
    ll.append_to_tail(1)
    ll.append_to_tail(2)
    ll.append_to_tail(3)
    ll.append_to_tail(4)

    # Creating a loop for testing
    ll.head.next.next.next.next = ll.head

    if detect_loop(ll.head):
        print("Loop detected")
    else:
        print("No loop detected")