#Monoalphabetic Substitution Cipher - Affine Cipher.
print ("\nSubi - Day 59 of #100DaysOfCode\n") 
print("\nMonoalphabetic Substitution Cipher - Affine Cipher\n")

n = input()
k1 = int(input())
k2 = int(input())
s=""
l=[*n]
l1 = []
for i in l:
    a = ord(i)-96
    c = ((k1*a)+k2)%26
    l1.append(c)
for i in l1:
    val =i+96
    v = chr(val)
    s = s+v
print(s)

from sympy import mod_inverse
k1_inverse = mod_inverse(k1,26)
m=""
l2=[*s]
l3=[]
for i in l2:
    a = ord(i)-96
    p = (k1_inverse*(a-k2))%26
    l3.append(p)
for i in l3:
    val =i+96
    v = chr(val)
    m = m+v
print(m)