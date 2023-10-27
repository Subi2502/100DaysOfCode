#Use the random module to generate random numbers and select random elements from a list.
print ("\nSubi - Day 39 of #100DaysOfCode\n") 
print("\nUse the random module to generate random numbers and select random elements from a list\n")

import random

list = [1, 2, 3, 4, 5]

elements = random.choices(list, k=3)

print(elements)


#Use the datetime module to work with dates and times.
print("\nUse the datetime module to work with dates and times\n")

from datetime import date 
  
my_date = date(1996, 12, 11) 
  
print("Date passed as argument is", my_date)


import datetime

date = datetime.date(2023, 3, 8)

time = datetime.time(14, 53, 55)

print(datetime.datetime.combine(date, time))