                              # 1 sololearn

                               # 2


set1 = {21, 32, 36, 14}
print(set1)

set1.add(3)
print(set1)

set1.remove(3)
print(set1)

set1.discard(2)
print(set1)

popped_element_from_set = set1.pop()
print(popped_element_from_set)
print(set1)

set1.clear()
print(set1)
                                # 3

dictionary1 = {
    "name": "luka",
    "age": 15,
    "city": "Tbilisi"
}
print(dictionary1.keys())
                                 # 4

print(dictionary1.values())

                                 # 5

def AddToDatabase(name, surname, age):
    database = {}
    database["name"] = name
    database["surname"] = surname
    database["age"] = age
    print(database)


AddToDatabase("nika", "nikaze", 22)