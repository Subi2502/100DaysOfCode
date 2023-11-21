#Transposition Cipher - Columnar cipher.
print ("\nSubi - Day 63 of #100DaysOfCode\n") 
print("\nTransposition Cipher - Columnar cipher\n")

r = int(input())
c  = int(input())
mat = [[0 for _ in range(c)] for _ in range(r)]
t_mat = [[0 for _ in range(r)] for _ in range(c)]
for i in range(r):
    for j in range(c):
        val = input("Enter the value:")
        mat[i][j] = val
print("Input:\n",mat)

r = c
c = r
for i in range(c):
    for j in range(r+1):
      t_mat[i][j] = mat[j][i]
print("Output:\n",t_mat)

for i in range(r+1):
    for j in range(c-1):
        mat[i][j]=t_mat[j][i]
print("Message:\n",mat)