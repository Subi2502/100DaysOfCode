#Write a python program to find the maximum of three numbers using if-else statements. 
print ("\nSubi - Day 14 of #100DaysOfCode\n") 
print("\nthe maximum of three numbers\n")

a, b, c = 2, 6, 8
if a > b and a > c:
    print(f"Maximum is {a}")
elif b > c and b > a:
    print(f"Maximum is {b}")
elif c > a and c > b:
    print(f"Maximum is {c}")
else:
    print(a)