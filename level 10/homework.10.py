                        #1
age = int(input("How old are you? "))
for i in range(7):
    print(age)
                               #2
temperature=float(input("Enter the Temperature here: "))
unit=input("Enter the unit here (C/F): ")

if unit=="C":
    temperature=((9 * temperature ) / 5 + 32)
    print(f"The temperature in Fahrenheit is: {round(temperature, 1)} F°")
elif unit=="F":
    temperature=((temperature-32) *5 / 9)
    print(f"The temperature in Celsius is: {round(temperature, 1)} C°")
else:
    print(f"{unit} is not valid!!!")

#if + or
temperature=25
is_snowing=True

if temperature>=35 or temperature<=0 or is_snowing:
    print("Sadly you can't go outside today😢")
else:
    print("You are free to go outside😀")

print("------------------------------------------------------------")
#if + and
price=50
is_traffic_jam=False

if price<=60 and is_traffic_jam:
    print("You can't by the new cod😢 ")
else:
    print("You can buy the new cod 😉")
print("--------------------------------------------------------------")
#if+not

ticket_price=20
is_mom_angry=True
is_raining=False

if not ticket_price<12 and not is_mom_angry and not is_raining:
    print("You can go😉")
elif not ticket_price>12 and not is_mom_angry and not is_raining:
    print("Maybe ask your parents for cash💵💵💵")
elif not ticket_price<12 and  is_mom_angry and not is_raining:
    print("Your mom needs to chill first😡😡😡")
elif not ticket_price<12 and not is_mom_angry and  is_raining:
    print("look outside first🌧⛈")
elif not ticket_price>12 and is_mom_angry and not is_raining:
    print("no money💵 and your mom is mad 😡")
elif not ticket_price>12 and not is_mom_angry and  is_raining:
    print("no money💵 and look outside first🌧⛈")
elif not ticket_price<12 and  is_mom_angry and  is_raining:
    print(" your mom is mad 😡 and look outside first🌧⛈")
elif not ticket_price>12 and  is_mom_angry and  is_raining:
    print("You suck stay home!!!")
                     #4

from turtle import *

for i in range(3):
    forward(200)
    left(120)

    exitonclick()



                        #5

name=input("Enter your age: ")

if name==20:
    print("True")
else:
    print("False")



