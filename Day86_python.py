#Write a program to perform binary tree level order traversal.
print ("\nSubi - Day 86 of #100DaysOfCode\n") 
print("\nWrite a program to perform binary tree level order traversal\n")

from queue import Queue

class binaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    def insert(root, newValue):
        if root is None:
            root = binaryTreeNode(newValue)
            return root
        if newValue<root.data:
            root.leftChild = insert(root.leftChild, newValue)
        else:
            root.rightChild = insert(root.leftChild, newValue)
        return root
    def levelorder(root):
        if root == None:
            return
        Q = Queue()
        Q.put(root)
        while(not Q.empty()):
            node = Q.get()
            if node == None:
                continue
            print(node.data)
            Q.put(node.leftChild)
            Q.put(node.rightChild)

    root = insert(None, 5)
    insert(None, 10)
    insert(None, 15)
    insert(None, 20)
    insert(None, 25)
    insert(None, 30)
    insert(None, 35)
    print("Printing the level order traversal of the binary tree.")
    levelorder(root)