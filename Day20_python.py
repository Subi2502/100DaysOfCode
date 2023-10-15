#Print the multiplication table of a number using nested loops.
print ("\nSubi - Day 20 of #100DaysOfCode\n") 
print("\nPrint the multiplication table of a number using nested loops.\n")

print("\t\t\t\tMultiplication Tables\n")
for i in range(1,13):
    print(i, end="\t")
print()
print("____________________________________________________________________\n")
for j in range(1,13):
    for k in range(1,13):
        print(j * k, end ="\t")
    print("\n")


#Implement a program to check if a year is a leap year using if-else statements.
print("\na program to check if a year is a leap year using if-else statements\n")

year = int(input("Enter year to be checked:"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("The year is a leap year!")
        else:
            print("The year is not a leap year!")
    else:
        print("The year is a leap year!")
else:
    print("The year is not a leap year!")