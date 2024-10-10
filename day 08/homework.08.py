#1 age

age=int(input("Enter your age here: "))
if 13<age<19:
    print("Access granted")
elif age>19:
    print("Access denied!!!")
elif age<13:
    print("Access denied!!!")
#2 exam points
point=int(input("Enter your points (1-10): "))
if point>=9:
    is_A=True
    print("is_A")
elif point==8:
    is_B=True
    print("is_B")
elif point==7:
    is_C=True
    print("is_C")
elif point==6:
    is_D=True
    print("is_D")
elif point<6:
    is_F=True
    print("is_F")
#3 game kills / logical operators

kill_counter=int(input("Enter your in game kills here: "))
used_hack=input("Have you ever used hacks (T/F): ")
if used_hack=="T" and kill_counter<=0:
    used_hack=True
    print("You suck you cheater with 0 kills")
elif used_hack=="F" and kill_counter<=0:
    used_hack=False
    print("player with no kills at least you are not hacking")
elif used_hack=="T" and kill_counter>0:
    used_hack=True
    print(f"cheater with {kill_counter} kills how surprising")
elif used_hack=="F" and kill_counter>0:
    used_hack=False
    print(f"player with {kill_counter} kills good job!!!")
else:
    print("Type correctly")
#4 int input
num1=int(input("Enter 1st number here: "))
num2=int(input("Enter 2nd number here: "))

print(num1==num2)
print(num1<num2)
print(num1>num2)
print(num1<=num2)
print(num1>=num2)
print(num1!=num2)
print("-------------------------------------------------------")
# 5 abc
a=5
b=7
c=2

if a > b > c:
    is_a_greatest = True
    is_b_middle=True
    is_c_least=True
    print("is_a_greatest is_b_middle is_c_least")
elif a > b < c:
    is_a_greatest = True
    is_b_least=True
    is_c_middle=True
    print("is_a_greatest is_b_least is_c_middle")

elif b> a > c:
    is_b_greatest = True
    is_a_middle = True
    is_c_least = True
    print("is_b_greatest is_a_middle is_c_least")
elif b> a < c:
    is_b_greatest = True
    is_c_middle = True
    is_a_least = True
    print("is_b_greatest is_c_middle is_a_least")
elif c> a > b:
    is_c_greatest = True
    is_a_middle = True
    is_b_least = True
    print("is_c_greatest  is_a_middle is_b_least")
elif c> a < b:
    is_c_greatest = True
    is_b_middle = True
    is_a_least = True
    print("is_c_greatest, is_b_middle, is_a_least")
else:
    print("the cant be equal")
print("----------------------------------------------------------------------------")
#6 score
score=int(input("Enter your score: "))
if score==100:
    is_perfect=True
    print("You have a perfect score ✔")
elif 50 <= score < 75:
    is_pass=True
    print("You passed ✔")
elif score>=75 and score!=100:
    is_high_pass=True
    print("You get a high pass ✔")
elif score<50:
    is_fail=True
    print("You failed ❌")
else:
    print(f"Wrong {score} ❌❌❌")
#7 p and q
print("-----------------------------------------------------")
P=False
Q=False

if P==True and Q==False:
    P_and_not_Q=True
    print("P_and_not_Q")
elif not P==True and not Q==True:
    not_P_and_Q=True
    print("not_P_and_Q")
elif P==True or Q==True:
    P_or_Q=True
    print("P and Q")
