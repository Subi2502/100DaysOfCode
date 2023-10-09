#Implement a simple guessing game where the user has to guess a number
print ("\nSubi - Day 17 of #100DaysOfCode\n") 
print("\na simple guessing game where the user has to guess a number\n")

import random
num = random.randint(1, 10)
guess = None
while guess != num:
    guess = input("guess a number between 1 and 10: ")
    guess = int(guess)
    if guess == num:
        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")

#Use a for loop to iterate through a string and count the number of vowels
print("\nfor loop to iterate through a string and count the number of vowels\n")

String = input('Enter the string :')
count = 0
string = String.lower()
for i in string:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i =='u':
        count +=1
if count == 0:
    print('No vowels found')
else:
    print('Total vowels are :' + str(count))