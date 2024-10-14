#birtday calculator

birth_year=int(input("Enter your birth year here: "))
did_have=input("did you already have your birthday in 2024 (Y/N): ")
if did_have=="Y" and birth_year<=1900:
    age = 2024 - birth_year
    print(f"How are you alive??? you are {age} years old")
elif did_have == "Y":
     age = 2024 - birth_year
     print(f"you are {age} years old ")
elif did_have == "N" and birth_year <= 1900:
    age = 2024 - birth_year - 1
    print(f"How are you alive??? you are {age} years old")
elif did_have=="Y" and birth_year>2024:
    age= 2024 - birth_year
    print(f"you aren't even born yet!!! you are {age} years old")
elif did_have=="N" and birth_year>2024:
    age= 2024 - birth_year
    print(f"you aren't even born yet!!! you are {age} years old")
elif did_have == "N":
    age = 2024 - birth_year - 1
    print(f"you are {age} years old" )
else:
    print(f"type your info correctly!!!")

#area calculator of  a square

which=input("What do you want to calculate area or the perimeter (A/P): ")
#Area
if which=="A":
    length = float(input("Enter the length of a rectangle here: "))
    width = float(input("Enter the width of a rectangle here: "))
    area_rectangle=length*width
    print(f"the area of a rectangle is {area_rectangle} cm² ")
#perimeter
elif which=="P":
    length = float(input("Enter the length of a rectangle here: "))
    width = float(input("Enter the width of a rectangle here: "))
    perimeter_rectangle=2*(length+width)
    print(f"the perimeter of a rectangle is {perimeter_rectangle} cm ")

#length from school to home converter
unit1=input("Enter an unit (Km/M): ")
len_school_to_home=float(input("Enter the distance from home to school: "))
if unit1=="Km":
    result=len_school_to_home*100
    print(f"the result in M is {result}m ")
elif unit1=="M":
    result=len_school_to_home/100
    print(f"the result in km is {result}km ")

#M TO CM TO MM
num1=float(input("Enter a number: "))

result1=num1*100
print(result1)

result2=num1*10
print(result2)

#user input

name=input("Enter your name: ")
surname=input("Enter your surname: ")
moms_name=input("Enter your moms name: ")
dads_name=input("Enter your dads name: ")
color=input("Enter your favourite color: ")
car=input("Enter your favourite cars: ")
hobby1=input("Enter your 1st hobby: ")
hobby2=input("Enter your 2nd hobby: ")
hobby3=input("Enter your 3rd hobby: ")

print(f"{name} {surname} {moms_name} {dads_name} {color} {car} {hobby1} {hobby2} {hobby3}")

#5.
number = int(input("Enter Number> "))

first = number // 10

second = number % 10

print(first + second)
