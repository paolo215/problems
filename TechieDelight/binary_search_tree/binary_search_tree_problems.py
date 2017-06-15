from Node import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None 

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            return

        self.__insert(self.root, value)

    def __insert(self, root, value):
        if root == None:
            root = Node(value)
            print(root.getValue())
            return

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

    def inorder(self, data):
        self.__inorder(self.root, data)

    def __inorder(self, root, data):
        if root == None:
            return
        self.__inorder(root.getLeft(), data)
        data.append(root.getValue())
        self.__inorder(root.getRight(), data)
    
    
   
