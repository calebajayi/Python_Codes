class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return "name:{}, age:{}, address:{}".format(self.name, self.age, self.address)


p1 = Person("John", 36, "Sycamores")
print(p1)

# Exercise 1


class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author

    def __str__(self):
        return "isbn:{}, title:{}, author:{}".format(self.isbn, self.title, self.author)


b1 = Book(000000, "The love of software", "Caleb")
print(b1)

# Exercise 3


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return "balance:{}".format(self.balance)

    def deposit(self, deposit):
        self.balance += deposit

    def withdraw(self, withdraw):
        self.balance -= withdraw

    def get_balance(self):
        return self.balance


b1 = BankAccount(50)
print(b1)
b1.deposit(20)
print('New balance after deposit:', b1)
b1.withdraw(40)
print('New balance after withdrawing:', b1)
print(b1.get_balance())

# Exercsie 4


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return "name:{}, age:{}, address:{}".format(self.name, self.age, self.address)

    def older(self, some_person):
        x = self.age - some_person.age
        if x > 0:
            return True
        elif x == 0:
            print("Same age")
        else:
            return False


p1 = Person("John", 36, "Sycamores")
p2 = Person("Mary", 50, "Offaly")
p3 = Person("Caleb", 26, "Kildare")

print(p1.older(p2))

# Advance Exercise


class Student:
    def __init__(self, name, number, marks=[]):
        self.name = name
        self.number = number
        self.marks = marks

    def __str__(self):
        return "name:{}, number:{}, marks:{}".format(self.name, self.number, self.marks)

    def avg_marks(self):
        return sum(self.marks) / len(self.marks)


s1 = Student("john", 3, marks=[15, 10, 5])

print(s1.avg_marks())

