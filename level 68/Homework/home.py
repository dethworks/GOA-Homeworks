#                                                         1
# დაწერეთ lambda-ფუნქცია, რომელიც იღებს რიცხვს და აბრუნებს მის გაორმაგებულ მნიშვნელობას.

duplicator = lambda num1 : num1 * 2

print(duplicator(4))

#                                                         2
# დაწერეთ lambda-ფუნქცია, რომელიც იღებს სტრინგს და აბრუნებს მის სიმბოლოების რაოდენობას.

# Whenever the condition is True (meaning i is one of those special characters),
# it generates 1. Essentially, this is a way of "counting" the occurrences.

symbol_counter = lambda str1: sum(1 for i in str1 if i in "!@#$%^&")

print(symbol_counter("Hello#!World&@!"))

#                                                         3
even_or_odd = lambda number : "Even" if number % 2 == 0 else "Odd"

print(even_or_odd(5))

#                                                         4
# რიცხვების კვადრატში აყვანა დაწერეთ lambda-ფუნქცია, რომელიც იღებს რიცხვს და აბრუნებს მის კვადრატს.

num_squared = lambda num1 : num1 ** 2

print(num_squared(7))

#                                                         5
# ლუწი რიცხვების კვადრატში აყვანა სიიდან
# დაწერეთ ფუნქცია, რომელიც lambda-ფუნქციას გამოიყენებს, რათა სიიდან ლუწი რიცხვები ამოარჩიოს და
# თითოეული მათგანი კვადრატში აიყვანოს.

even_squared = lambda arr : [ x ** 2 for x in arr if x % 2 == 0 ]

print(even_squared([1, 3, 4, 6]))











