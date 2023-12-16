#Write a program to check if a binary tree is balanced.
print ("\nSubi - Day 88 of #100DaysOfCode\n") 
print("\nWrite a program to check if a binary tree is balanced\n")

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_balanced(root):
    def check_height(node):
        if node is None:
            return 0

        left_height = check_height(node.left)
        right_height = check_height(node.right)

        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    return check_height(root) != -1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5)

if is_balanced(root):
    print("The binary tree is balanced.")
else:
    print("The binary tree is not balanced.")
