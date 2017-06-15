import unittest
import binary_search_tree_problems as bst
from Node import Node


class TestBinarySearchTree(unittest.TestCase):
    def test_insert(self):  
        tree = bst.BinarySearchTree()
        tree.insert(4)
        self.assertTrue(tree.root.getValue() == 4)

        tree.insert(2)
        self.assertTrue(tree.root.getLeft().getValue() == 2)


        tree.insert(6)
        self.assertTrue(tree.root.getRight().getValue() == 6)

        tree.insert(8)
        self.assertTrue(tree.root.getRight().getRight().getValue() == 8)

        tree.insert(5)
        self.assertTrue(tree.root.getRight().getLeft().getValue() == 5)



if __name__ == "__main__":
    unittest.main()
