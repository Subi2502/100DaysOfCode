#Polyaphabetic substitution Cipher - Vignere Cipher.
print ("\nSubi - Day 61 of #100DaysOfCode\n") 
print("\nPolyaphabetic substitution Cipher - Vignere Cipher\n")

msg = "helloworld"
key = "key"
alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher = []
if len(msg) != len(key):
  for i in range(len(msg)-len(key)):
    key = key + (key[i % len(key)])
print(f"key: {key}")
for m,k in zip(msg,key):
  x = (ord(m) + ord(k)) % 26
cipher.append(alphabet[x])
print(*cipher, sep="")


#Polyaphabetic substitution Cipher - hill cipher.
print("\nPolyaphabetic substitution Cipher - hill cipher\n")

import numpy as np

plain = input()
keys = input()

mat = [[(ord(keys[0])-ord('A'))%26, (ord(keys[1])-ord('A'))%26],[(ord(keys[2])-ord('A'))%26, (ord(keys[3])-ord('A'))%26]]

while len(plain)%len(keys)!=0:
  plain+='X'

num_txt = [ord(char)-ord('a') for char in plain]
k_mat = np.array(mat)
p_mat = np.array(num_txt).reshape(len(k_mat),-1)
e_mat = np.dot(k_mat,p_mat)%26
e_num_txt = e_mat.flatten().tolist()
e_txt = ''.join([chr(num+ord('a')) for num in e_num_txt])
print(mat)
print(e_txt)
