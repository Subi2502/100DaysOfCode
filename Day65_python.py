#swapping between two integers.
print ("\nSubi - Day 65 of #100DaysOfCode\n") 
print("\nswapping between two integers\n")

a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
c = a^b
d = c^b
c = c^d
print(c,d)


#XOR each character in this string.
print("\nXOR each character in this string\n")

a = "Helloworld"
for i in range(0, len(a)):
  b = ord(a[i])
  c = b^0
  d = b^127
  print(c,d)


#one-time padding.
print("\none-time padding\n")

a = input("enter a character:")
b = ord(a)
c = int(input("Enter the key value:"))
d = b^c
print("Cipher Text:",d)
e = d^c
print("Cipher Text xor with the key value:",e)
print("The input message is:",chr(e))