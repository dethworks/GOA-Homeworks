                            #1
name = "Two Tower"
result = ""

for i in name:
    result += i

print(result)
                           #2
num=int(input("Enter a number: "))

if num%2==0:
    print("Even")
else:
    print("ODD")
                            #3
for i in range(1, 101):
    if i % 2 == 0:
        print(f"{i} არის ლუწი")
    else:
        print(f"{i} არის კენტი")
                            #4
for i in range(-100,100):
    if i > 0:
        print(f"{i}Positive")
    else:
        print(f"{i}Negative")

#reverses name

name="name"
print(name[::-1])