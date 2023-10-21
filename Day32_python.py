#Create a class for a car with attributes like make, model, and year.
print ("\nSubi - Day 32 of #100DaysOfCode\n") 
print("\nCreate a class for a car with attributes like make, model, and year\n")

class Car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

  def __str__(self):
    return f"{self.year} {self.make} {self.model}"

car = Car('Tesla', 'Model S', 2012)

print(car)


#Implement a class for a bank account with methods for deposit and withdrawal.
print("\nImplement a class for a bank account with methods for deposit and withdrawal\n")

class Bank_Account:
  def __init__(self):
     self.balance = 0
     print("welcome to Unique bank, you can deposit and withdraw your money!")

  def deposit(self):
     amount = float(input("Enter amount to be deposit :"))
     self.balance += amount
     print("\n amount is deposited")
    
  def withdraw(self):
     amount = float(input("Enter amount to be withdraw :"))
     if amount >= self.balance:
         print("\n Insufficient Balance")
     else:
         self.balance -= amount
         print("\n Money is withdrawn")
  def display(self):
      print("Current Bank Balance is",self.balance)

bank_acc_object = Bank_Account()
bank_acc_object.display()
bank_acc_object.deposit()
bank_acc_object.display()
bank_acc_object.withdraw()
bank_acc_object.display()
bank_acc_object.withdraw()
bank_acc_object.display()
