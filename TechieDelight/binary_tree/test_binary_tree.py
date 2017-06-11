import binary_tree_problems as bt
from Node import Node
import unittest

class TestBinaryTree(unittest.TestCase):
    def test_isIdentical(self):
        a = Node(5)
        b = Node(5)

        self.assertTrue(bt.isIdentical(a, b))

        a = Node(5, Node(2, Node(3)), Node(5))
        b = Node(5, Node(2, Node(3)), Node(5))

        self.assertTrue(bt.isIdentical(a, b))

        a = Node(2)
        b = Node(3)
        self.assertTrue(not bt.isIdentical(a, b))

        a = Node(5, Node(3, Node(5, Node(10, Node(3)), Node(1)), 1), 2)
        b = Node(5, Node(3, Node(5, Node(10, Node(1)), Node(1)), 1), 2)
        self.assertTrue(not bt.isIdentical(a, b))


if __name__ == "__main__":
    unittest.main()
