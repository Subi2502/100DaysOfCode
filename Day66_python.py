#ElGamal.
print ("\nSubi - Day 66 of #100DaysOfCode\n") 
print("\nElGamal\n")

import random
from sympy import mod_inverse
p=int(input())
a=int(input())
x=int(input())
M=int(input())

y=(a**x)%p

k=int(input())
K=(y**k)%p
C1=(a**k)%p
C2=(K*M)%p

print(C1,C2)
K_1=(C1**x)%p
K_inv=mod_inverse(K_1,p)
P=(C2*K_inv)%p
print(P)