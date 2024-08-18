import unittest

from geeksforgeeks.datastructures.arrays.search_insert_delete_unsorted_array import UnsortedArray


class SearchInsertDeleteUnsortedArray(unittest.TestCase):

    def setUp(self) -> None:
        arr = [12, 34, 10, 6, 40]
        self.unsorted_array = UnsortedArray(arr)

    def test_search(self):
        x = 40
        self.assertEqual(self.unsorted_array.search(x), 4)

    def test_search_not_found(self):
        x = 100
        self.assertEqual(self.unsorted_array.search(x), -1)

    def test_search_empty_array(self):
        x = 100
        self.assertEqual(self.unsorted_array.search(x), -1)

    def test_insert(self):
        arr = [12, 34, 10, 6, 40]
        x = 100
        self.unsorted_array.insert(x)
        self.unsorted_array.search(x)
        self.assertEqual(self.unsorted_array.arr, [12, 34, 10, 6, 40, 100])

    def test_delete(self):
        x = 10
        self.unsorted_array.delete(x)
        index = self.unsorted_array.search(x)
        self.assertEqual(index, -1)
        self.assertEqual(self.unsorted_array.arr, [12, 34, 6, 40])


if __name__ == '__main__':
    unittest.main()
