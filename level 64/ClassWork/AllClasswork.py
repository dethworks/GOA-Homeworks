                              # 1
def repeat_str(r, s):
    return r * s

                               # 2
class human:
  def __init__(self, name, age, height, weight):
    self.name = name
    self.age = age
    self.height = height
    self.weight = weight

human1 = human("luka", 21, 165, 60)
human2 = human("nika", 13, 180, 80)

print(human1.name, human1.age, human1.height, human1.weight)
print(human2.name, human2.age, human2.height, human2.weight)

                            # 3
class Human:
    def __init__(self, name, surname, age, height, weight):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"{self.name} {self.surname}, Age: {self.age}, Height: {self.height}cm, Weight: {self.weight}kg"

    def print_name_and_surname(self):
        print(f"Name: {self.name}, Surname: {self.surname}")

    def print_age_height_weight(self):
        print(f"Age: {self.age}, Height: {self.height}cm, Weight: {self.weight}kg")


human1 = Human("Saba", "Chakvetaze", 21, 165, 60)
human2 = Human("Nika", "Nikaze", 13, 180, 80)

print(human1)
print(human2)











