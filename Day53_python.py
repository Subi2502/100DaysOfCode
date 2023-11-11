#Write a program to implement a binary tree and perform tree traversal (inorder, preorder, postorder).
print ("\nSubi - Day 53 of #100DaysOfCode\n") 
print("\nprogram to implement a binary tree and perform tree traversal (inorder, preorder, postorder)\n")

class NOde:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder_traversal(root):
    if root:
        
        inorder_traversal(root.left)
        inorder_traversal(root.right)
        print(root.val, end="")

def preorder_traversal(root):
    if root:

        preorder_traversal(root.left)
        preorder_traversal(root.right)
        print(root.val, end="")

def postorder_traversal(root):
    if root:

        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end="")


if __name__ == "__main__":
    root = NOde(0)
    root.left = NOde(8)
    root.right = NOde(6)
    root.left.left = NOde(4)
    root.left.right = NOde(2)

    print("Inorder Traversal:")
    inorder_traversal(root)
    print("\nPreorder Traversal:")
    preorder_traversal(root)
    print("\nPostorder Traversal:")
    postorder_traversal(root)

