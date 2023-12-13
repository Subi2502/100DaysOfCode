#Write a program to implement a binary search tree (BST).
print ("\nSubi - Day 84 of #100DaysOfCode\n") 
print("\nWrite a program to implement a binary search tree (BST)\n")

class Node:  
 def __init__(self, val):  
  self.val = val  
  self.left = None  
  self.right = None  
   
def search(root, x):  
  if root is None or root.val == x:  
    return root.val  
  if root.val < x:  
    return search(root.right, x)  
  return search(root.left, x)  
   
root = Node(9)  
root.left = Node(1)  
root.right = Node(10)  
root.left.left = Node(0)  
root.left.right = Node(3)  
root.left.right.right = Node(4)  
x = 4 
v = search(root, x)  
print("The node we are searching for is present in the given BST: ", v)