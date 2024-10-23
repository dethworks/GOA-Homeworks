                              #1
name = input("Enter a your name: ")

result = " "

for i in name:
    result += i + " "

print(result)
                              #2

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

for i in range(num1, num2 + 1):
    if num1 % 2 == 0 and num2 % 3 == 0:
        print("These numbers are multiples of 3 and 2")
    else:
        print("These numbers are not multiples of 3 and 2")
                                 #3

total = 0
for i in range(1):
    number1 = float(input("შეიყვანეთ ციფრი1: "))
    number2 = float(input("შეიყვანეთ ციფრი2: "))
    number3 = float(input("შეიყვანეთ ციფრი3: "))
    number4 = float(input("შეიყვანეთ ციფრი4: "))
    number5 = float(input("შეიყვანეთ ციფრი5: "))

    total += number1+number2+number3+number4+number5

average = total / 5
print(f"საშუალო არითმეტიკული: {average}")

                          #4

for i in range(-100,101):
    if i > 0:
        print(f"{i} Positive")
    else:
        print(f"{i} Negative")
                          #5
num6=int(input("Enter a positive number: "))

while not num6>=0:
    num6=int(input("Enter a positive number: "))

print(num6)