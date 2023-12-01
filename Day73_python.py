#Write a program to check if a binary tree is a binary search tree (BST).
print ("\nSubi - Day 73 of #100DaysOfCode\n") 
print("\nWrite a program to check if a binary tree is a binary search tree (BST)\n")

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def is_bst(root):
  if root is None:
    return True

  if root.left is not None and root.left.data >= root.data:
    return False

  if root.right is not None and root.right.data <= root.data:
    return False

  return is_bst(root.left) and is_bst(root.right)

def main():
  root = Node(10)
  root.left = Node(5)
  root.right = Node(15)

  if is_bst(root):
    print("The binary tree is a BST")
  else:
    print("The binary tree is not a BST")

if __name__ == "__main__":
  main()