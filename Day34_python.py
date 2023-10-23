#Write a program to demonstrate encapsulation in a class.
print ("\nSubi - Day 34 of #100DaysOfCode\n") 
print("\nWrite a program to demonstrate encapsulation in a class\n")

class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

    def display_info(self):
        print(f"Account Number: {self._account_number}")
        print(f"Balance: {self.__balance}")


account = BankAccount("21212524", 4000.00)

account.display_info()

account.deposit(5000)
account.withdraw(3000)

print(f"Updated Balance: {account.get_balance()}")


#Implement a class for a library with books and patrons.
print("\nImplement a class for a library with books and patrons\n")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False 

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"The book '{self.title}' by {self.author} has been checked out."
        else:
            return f"The book '{self.title}' is already checked out."

    def check_in(self):
        if self.checked_out:
            self.checked_out = False
            return f"The book '{self.title}' has been checked in."
        else:
            return f"The book '{self.title}' is not checked out."

    def __str__(self):
        return f"'{self.title}' by {self.author}"

class Patron:
    def __init__(self, name):
        self.name = name
        self.checked_out_books = []

    def check_out_book(self, book):
        if book.checked_out:
            return f"Sorry, '{book.title}' is already checked out."
        else:
            book.check_out()
            self.checked_out_books.append(book)
            return f"'{book.title}' has been checked out by {self.name}."

    def return_book(self, book):
        if book in self.checked_out_books:
            self.checked_out_books.remove(book)
            book.check_in()
            return f"'{book.title}' has been returned by {self.name}."
        else:
            return f"'{book.title}' was not checked out by {self.name}."

    def __str__(self):
        return self.name

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def add_patron(self, patron):
        self.patrons.append(patron)

    def list_books(self):
        return [str(book) for book in self.books]

    def list_patrons(self):
        return [str(patron) for patron in self.patrons]


book1 = Book("The Secret", "Rhonda Byrne")
book2 = Book("Can't Hurt Me", "David Goggins")
patron1 = Patron("John")
patron2 = Patron("David")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_patron(patron1)
library.add_patron(patron2)

print(patron1.check_out_book(book1))
print(patron2.check_out_book(book2))
print(patron1.return_book(book1))

print("Books in the library:")
print(library.list_books())
print("Patrons in the library:")
print(library.list_patrons())
