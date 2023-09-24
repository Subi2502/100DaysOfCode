
# Calculate the area of a triangle  
print ("\nSubi - Day 5 of #100DaysOfCode\n")
print("\narea of a triangle \n")

a = int(input("Enter the length of first side :"))
b = int(input("Enter the length of second side :"))
c = int(input("Enter the length of third side :"))
P = (a+b+c)
s = P/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("area of triangle is:",area)
print("perimeter of triangle is:",P)
print("semi perimeter of triangle is:",s)