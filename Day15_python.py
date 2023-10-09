#Implement a while loop to print numbers from 1 to 10  
print ("\nSubi - Day 15 of #100DaysOfCode\n") 
print("\nwhile loop to print numbers from 1 to 10\n")

input = 1
while input <= 10:
     print(input)
     input +=1


#Use a for loop to iterate through a list and print each element     
print("\nfor loop to iterate through a list and print each element\n")

pets = ['dog', 'cat', 'monkey', 'fish', 'snake']
print(pets)
for pet in pets:
     print(pet)
for index in range(len(pets)):
     value = pets[index]
     print(f'{index}:{value}')
for pet in enumerate(pets):
     print(pet)
list = [1, 2, 3]     
print(max(list))     
print(min(list))
print(sum(list))      