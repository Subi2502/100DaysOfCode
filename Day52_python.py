#Write a program to find the intersection point of two linked lists.
print ("\nSubi - Day 52 of #100DaysOfCode\n") 
print("\nprogram to find the intersection point of two linked lists\n")

class listNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def find_intersection(head1, head2):
    
    def get_length(node):
        length = 0
        while node:
            length +=1
            node = node.next
        return length
    
    len1 = get_length(head1)
    len2 = get_length(head2)

    current1 = head1
    current2 = head2

    if len1 > len2:
        for _ in range(len1 - len2):
            current1 = current1.next
    elif len2 > len1:
        for _ in range(len2 - len1):
            current2 = current2.next

while current1 != current2:
    current1 = current1.next
    current2 = current2.next

def my_function():
    return (current1)
    
common_node = listNode(10)
list1 = listNode(0)
list1.next = listNode(5) 
list1.next.next = common_node
list2 = listNode(6)
list2.next = common_node

intersection_node = find_intersection(list1, list2)
if intersection_node:
    print("Intersection point value:", intersection_node.value)
else:
    print("No intersection found")