from Node import Node

def insert(root, value):
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

def inorder(root, data):
    if root == None:
        return
    inorder(root.getLeft(), data)
    data.append(root.getValue())
    inorder(root.getRight(), data)
    
    
