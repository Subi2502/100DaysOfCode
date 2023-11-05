#Create a data visualization using a library like Matplotlib
print ("\nSubi - Day 47 of #100DaysOfCode\n") 
print("\nCreate a data visualization using a library like Matplotlib\n")

import matplotlib.pyplot as plt

Group = ['Group A', 'Group B', 'Group C', 'Group D']
Grade = ['B', 'C', 'A', 'D']

plt.bar(Group, Grade)

plt.xlabel('Group')
plt.ylabel('Grade')
plt.title('Bar Chart Example')

plt.show()


#Create a data visualization using a library like Seaborn
print("\nCreate a data visualization using a library like Seaborn\n")

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.histplot(data=tips, x="total_bill", bins=20, kde=True)

plt.title("Histogram of Total Bill Amounts")

plt.xlabel("Total Bill Amount")
plt.ylabel("Frequency")

plt.show()
