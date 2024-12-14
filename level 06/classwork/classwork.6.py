                             #1

name = input("enter your name: ")
surname = input("enter your surname: ")

full_name = name + " " + surname

print("full name:", full_name)
                             #2

name1 = float(input("enter first number: "))
name2 = float(input("enter second number: "))


operator = input("select a operator (+, -, //, /, *, **): ")

if operator == "+":
    result = name1 + name2
elif operator == "-":
    result = name1 - name2
elif operator == "//":
    result = name1 // name2
elif operator == "/":
    result = name1 / name2
elif operator == "*":
    result = name1 * name2
elif operator == "**":
    result = name1 ** name2
else:
    result = "incorrect operator"

print("result: ", result)

