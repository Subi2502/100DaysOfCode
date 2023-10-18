#Create a set and perform various set operations (union, intersection, etc.)
print ("\nSubi - Day 29 of #100DaysOfCode\n") 
print("\nCreate a set and perform various set operations - union, intersection,\n")

s1 = {0, 1, 2}
s2 = {1, 2, 3}
s3 = {2, 3, 4}

print(s1.union(s2))

s1 = {0, 1, 2}
s2 = {1, 2, 3}
s3 = {2, 3, 4}

print(s1.intersection(s2, s3))


#Implement a linked list data structure.
print("\nImplement a linked list data structure\n")

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def insert(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      current_node = self.head
      while current_node.next is not None:
        current_node = current_node.next
      current_node.next = new_node

  def print(self):
    current_node = self.head
    while current_node is not None:
      print(current_node.data)
      current_node = current_node.next

linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.print()