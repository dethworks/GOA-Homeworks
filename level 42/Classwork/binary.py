age = int(input("Enter your age: "))
binary_age = ""

while age > 0:
    binary_age = str(age % 2) + binary_age
    age = age // 2

print(f"Your age in binary is: {binary_age}")