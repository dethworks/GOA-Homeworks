                           #1

num1=int(input("Enter a number: "))

if num1 < 10:
    print("Your number is less than 10")
else:
    print("Your number is not less than 10")

                            #2

num2=int(input("Enter a number: "))

if num2%2==0:
    print("Your number is Even")
else:
    print("Your number is Odd")

                            #3

num3=int(input("Enter a number: "))

if num3>0:
    print("Your number is positive")
elif num3==0:
    print("Your number is 0")
else:
    print("Your number is Negative")

                             #4

num4=int(input("Enter 1st number: "))
num5=int(input("Enter 2nd number: "))

if num4==num5:
    print("Numbers are equal")
else:
    print("Numbers are not equal")
                              #5

num6=int(input("Enter a number: "))

if num6>100 and num6%2==0:
    print("Your number is more than 100 and Even")
elif num6==100:
    print("Your number is 100")
elif num6<100 and num6%2==0:
    print("Your number is not more than 100 but is Even")
elif num6>100 and num6%2!=0:
    print("Your number is more than 100 but is Odd")
else:
    print("Your number is not more than 100 and it is Odd")

                           #6

num7=int(input("Enter a number: "))

if num7%5==0 and num7%10==0:
    print("True")
else:
    print("False")

                         #7
for i in range(5):
    print(' ' * (4 - i) + '*' * (2 * i + 1))

