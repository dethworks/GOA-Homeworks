#1
user_name=input("Enter your user name: ")
last_name=input("Enter your last name: ")
age=int(input("Enter your age "))
print("Result:")
print(f"Your name is {user_name}")
print(f"Your last name is {last_name}")
print(f"You are {age} years old")

#2
print("-------------------------------------------------------------------------------")

num1=float(input("Enter 1st number : "))
num2=float(input("Enter 2nd number : "))
operator=input("Select an operator: + - * /: ")

if operator=="+":
    result=num1+num2
    print(f"{round(result, 2)}")
elif operator=="-":
    result=num1-num2
    print(f"{round(result, 2)}")
elif operator=="*":
    result=num1*num2
    print(f"{round(result, 2)}")
elif operator=="/":
    result=num1/num2
    print(f"{round(result, 2)}")
else:
    print(f"The operator {operator} is not Valid!!!")

#3
print("---------------------------------------------------------------------------------")

user1=input("Enter your name: ")
print(f"{user1}")

#4
print("-----------------------------------------------------------------------------------")


math1 = 20 + 20
math2 = math1 - 10
math3 = math2 * 2

print(f"{math3}")

#5
print("---------------------------------------------------------------------------------------")

academy=input("Enter your academy: ")
school=input("Enter your school: ")
Name=input("Enter your name: ")
Last_name=input("Enter your last name: ")
print("Result:")
print(f"Your academy is {academy}")
print(f"Your school is {school}")
print(f"Your name is {Name}")
print(f"Yor last name is {Last_name}")





