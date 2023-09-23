#Write a program to print the first 10 prime numbers. 
print ("\nSubi - Day 4 of #100DaysOfCode\n")
print("\nprint the first 10 prime numbers\n")

r=10  
for a in range(2,r+1):  
    k=0  
    for i in range(2,a//2+1):  
        if(a%i==0):  
            k=k+1  
    if(k<=0):  
        print(a,end=" ")  