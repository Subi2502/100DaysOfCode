#Implement DSS using DSA.
print ("\nSubi - Day 55 of #100DaysOfCode\n") 
print("\nImplement DSS using DSA\n")

import random
p = int(input("p:"))
q = int(input("q:"))
x = int(input("Private_key:"))
M = int(input("Hashed_Message:"))
h = random.randint(2, p-2)
g = int(h**((p-1)/q))
print(h,g)
y = (g**x)%p
k = random.randint(1, q-1)
print("public_key:",y)
print("Random Integer:",k)
r = ((g**k)%p)%q
for i in range(1,q):
    if k*i%q == 1:
        s = (1*(M + x*r))%q
        break
    dig_sign = [r,s]

    print("Digital_Signature:",dig_sign[1])
    w = 0
    r,s = dig_sign[0], dig_sign[1]
    for i in range(2,20):
        if(i*s)%q == 1:
            w = i
            break
        u1 = (M * w)%q
        u2 = (r * w)%q
        v = (((g ** u1)*(y**u2))%p)%q

        print('w:',w)
        print('u1:',u1)
        print('u2:',u2)
        print('v:',v)
        
        if v == r:
            print("Signature is Verified")
        else:
            print("Signature is not Verified")