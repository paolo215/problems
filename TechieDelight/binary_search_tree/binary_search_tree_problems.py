from Node import Node

class BinarySearchTree:
    # Binary Search Tree data structure. Assumes that the values of the Nodes
    # are numbers.
    def __init__(self):
        self.root = None 

    # Wrapper for inserting value to BST
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            return

        self.__insert(self.root, value)

    # Recursive insertion BST
    def __insert(self, root, value):
        if root == None:
            root = Node(value)
            print(root.getValue())
            return

        # Go to the right if value >= value of the root
        if value >= root.getValue():
            if root.getRight():
                insert(root.getRight(), value)
            else:
                root.setRight(Node(value))
        else:
            if root.getLeft():
                insert(root.getLeft(), value)
            else:
                root.setLeft(Node(value))

    
    # Wrapper for inorder traversal
    def inorder(self, data):
        self.__inorder(self.root, data)

    # Inorder traversal
    def __inorder(self, root, data):
        if root == None:
            return
        self.__inorder(root.getLeft(), data)
        data.append(root.getValue())
        self.__inorder(root.getRight(), data)
    
    
   
