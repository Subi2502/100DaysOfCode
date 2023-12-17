#Write a program to implement a linked list class.
print ("\nSubi - Day 89 of #100DaysOfCode\n") 
print("\nWrite a program to implement a linked list class\n")

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    last_node = self.head
    while last_node.next is not None:
      last_node = last_node.next
    last_node.next = new_node

  def display(self):
    current_node = self.head
    while current_node is not None:
      print(current_node.data)
      current_node = current_node.next

if __name__ == '__main__':
  llist = LinkedList()
  llist.append(1)
  llist.append(2)
  llist.append(3)

  llist.display()
