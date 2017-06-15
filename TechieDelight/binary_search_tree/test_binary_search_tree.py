import unittest
import binary_search_tree_problems as bst
from Node import Node


class TestBinarySearchTree(unittest.TestCase):
    def test_insert(self):  
        tree = bst.BinarySearchTree()
        tree.insert(4)
        tree.insert(2)

        inorder_output = []
        tree.inorder(inorder_output)
        expected = [2, 4]

        self.assertTrue(expected == inorder_output)


if __name__ == "__main__":
    unittest.main()
