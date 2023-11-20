#Transposition Cipher - Rail Fence Cipher.
print ("\nSubi - Day 62 of #100DaysOfCode\n") 
print("\nTransposition Cipher - Rail Fence Cipher\n")

n = input("Enter the plain text:")
even = ""
odd = ""
for i in n:
    if(n.index(i)%2==0):
        even = even+i
    else:
        odd = odd+i
print(even+odd)

c = even+odd
half_length = len(c) // 2
decrypted_text = ""

for i in range(half_length):
    decrypted_text += even[i] + odd[i]
print(decrypted_text)