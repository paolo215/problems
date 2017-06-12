import unittest
import binary_search_tree_problems as bst
from Node import Node


class TestBinarySearchTree(unittest.TestCase):
    def test_insert(self):  
        root = Node(4)
        bst.insert(root, 2)

        inorder_output = []
        bst.inorder(root, inorder_output)
        expected = [2, 4]

        self.assertTrue(expected == inorder_output)


if __name__ == "__main__":
    unittest.main()
