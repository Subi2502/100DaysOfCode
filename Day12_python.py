#Remove duplicate elements from a list
print ("\nSubi - Day 12 of #100DaysOfCode\n") 
print("\nRemove duplicate elements from a list\n")

test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print("The original list is : " + str(test_list))
 
res = []
for i in test_list:
    if i not in res:
        res.append(i)
        print("The list after removing duplicates : " + str(res))