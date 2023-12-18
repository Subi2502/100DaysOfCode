#Write a program to implement a stack using a linked list.
print ("\nSubi - Day 90 of #100DaysOfCode\n") 
print("\nWrite a program to implement a stack using a linked list\n")

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None

  def push(self, data):
    new_node = Node(data)
    new_node.next = self.top
    self.top = new_node

  def pop(self):
    if self.top is None:
      return None
    else:
      data = self.top.data
      self.top = self.top.next
      return data

  def peek(self):
    if self.top is None:
      return None
    else:
      return self.top.data

  def is_empty(self):
    return self.top is None

myStack = Stack()
myStack.push(1)
myStack.push(2)
myStack.push(3)

print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())