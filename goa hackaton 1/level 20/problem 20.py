operator = input("Enter a operator (+ * / -): ")
num1 = float(input("Enter a num1: "))
num2 = float(input("Enter num2: "))


if operator =="+":
    print(num1+num2)
elif operator =="-":
    print(num1-num2)
elif operator =="*":
    print(num1*num2)
elif operator =="/":
    print(num1/num2)    
else:
    print("INVALID")