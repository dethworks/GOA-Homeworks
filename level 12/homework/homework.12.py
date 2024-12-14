#1
for i in range(1, 51, 2):
    print(i)
print("----------------------------------------------------")
i = 1
while i <= 50:
    print(i)
    i += 2
print("----------------------------------------------------")
#2
width1=10
for width1 in range(2):
    print("****")
print("----------------------------------------------------")
#3
width1=20
for width1 in range(2):
    print("******")
#4
for num1 in range(0, 20, 3):
    for num2 in range(0, 20, 2):
        print(num1, num2)
#5
real_username="Dude"
real_password="Dude2009"
print("Log in")
username=input("Enter a username: ")
while username != real_username:
    print("Username Not found!")
    username=input("Renter your username: ")

print("Username found ✔")

password=input("Enter your password: ")

while password != real_password:
    print("Password incorrect! Try again! ")
    password=input("Renter your password: ")

print("Password correct")
print("Access Granted ✔")

