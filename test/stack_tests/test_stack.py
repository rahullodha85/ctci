import unittest

from stack.stack import Stack


class StackTests(unittest.TestCase):
    def test_is_empty(self):
        stack = Stack()

        self.assertTrue(stack.is_empty())

    def test_peek(self):
        stack = Stack()
        self.assertIsNone(stack.peek())

        stack = Stack(1)
        self.assertEqual(1, stack.peek())

    def test_push(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(1, stack.peek())

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(1, stack.pop())

    def test_pop_empty(self):
        stack = Stack()
        with self.assertRaises(Exception) as e:
            stack.pop()
        self.assertEqual("stack is empty", str(e.exception))


if __name__ == '__main__':
    unittest.main()
