import math

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(f"{dog1.name} is {dog1.age} years old.")
print(f"{dog2.name} is {dog2.age} years old.")


class Car:
    def drive(self):
        print("The car is driving")

    def stop(self):
        print("The car has stopped")

car = Car()
car.drive()
car.stop()


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

c = Circle(4)
print(c.area())


class Student:
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    def introduce(self):
        print(f"My name is {self.name}, I study {self.subject} and my grade is {self.grade}.")

s = Student("Giorgi", 10, "Math")
s.introduce()


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

acc = BankAccount()
acc.deposit(200)
acc.withdraw(50)
acc.withdraw(200)
