"""sum linked-lists by elements tests"""

import unittest

from linkedlist.linked_list import LinkedList
from linkedlist.sum_list import sum_list


class TestSumList(unittest.TestCase):
    """sum linked-lists by elements tests"""
    def test_sum_list(self):
        """smoke test"""
        linked_list_1 = LinkedList()
        linked_list_1.append_to_tail(7)
        linked_list_1.append_to_tail(1)
        linked_list_1.append_to_tail(6)

        linked_list_2 = LinkedList()
        linked_list_2.append_to_tail(5)
        linked_list_2.append_to_tail(9)
        linked_list_2.append_to_tail(2)

        expected_result = LinkedList(2)
        expected_result.append_to_tail(1)
        expected_result.append_to_tail(9)

        result_list = sum_list(linked_list_1, linked_list_2)

        result_list_curr = result_list.top
        expected_result_curr = expected_result.head
        while result_list_curr and expected_result_curr:
            self.assertEqual(expected_result_curr.data, result_list_curr.data)
            result_list_curr = result_list_curr.next
            expected_result_curr = expected_result_curr.next

        self.assertIsNone(result_list_curr)
        self.assertIsNone(expected_result_curr)

    def test_sum_list_one_short(self):
        """one linked list is shorter than other"""
        linked_list_1 = LinkedList()
        linked_list_1.append_to_tail(7)
        linked_list_1.append_to_tail(1)

        linked_list_2 = LinkedList()
        linked_list_2.append_to_tail(5)
        linked_list_2.append_to_tail(9)
        linked_list_2.append_to_tail(2)

        expected_result = LinkedList(2)
        expected_result.append_to_tail(1)
        expected_result.append_to_tail(3)

        result_list = sum_list(linked_list_1, linked_list_2)

        result_list_curr = result_list.top
        expected_result_curr = expected_result.head
        while result_list_curr and expected_result_curr:
            self.assertEqual(expected_result_curr.data, result_list_curr.data)
            result_list_curr = result_list_curr.next
            expected_result_curr = expected_result_curr.next

        self.assertIsNone(result_list_curr)
        self.assertIsNone(expected_result_curr)

    def test_sum_list_one_empty(self):
        """one linked list is empty"""
        linked_list_1 = LinkedList()

        linked_list_2 = LinkedList()
        linked_list_2.append_to_tail(5)
        linked_list_2.append_to_tail(9)
        linked_list_2.append_to_tail(2)

        expected_result = LinkedList(5)
        expected_result.append_to_tail(9)
        expected_result.append_to_tail(2)

        result_list = sum_list(linked_list_1, linked_list_2)

        result_list_curr = result_list.top
        expected_result_curr = expected_result.head
        while result_list_curr and expected_result_curr:
            self.assertEqual(expected_result_curr.data, result_list_curr.data)
            result_list_curr = result_list_curr.next
            expected_result_curr = expected_result_curr.next

        self.assertIsNone(result_list_curr)
        self.assertIsNone(expected_result_curr)


if __name__ == '__main__':
    unittest.main()
