import unittest

from geeksforgeeks.datastructures.arrays.search_insert_delete_sorted_array import SortedArray


class SortedArrayTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sorted_array = SortedArray([1, 2, 3, 4, 5])

    def test_search(self):
        self.assertEqual(self.sorted_array.search(self.sorted_array.arr, 3), 2)
        self.assertEqual(self.sorted_array.search(self.sorted_array.arr, 6), -1)

    def test_search_empty(self):
        self.assertEqual(self.sorted_array.search([], 3), -1)


if __name__ == '__main__':
    unittest.main()
