def two_sort(array):
    array.sort()
    return '***'.join(array[0])

                                                 #2


class Person:
  def __init__(self, name, surname, dad_name):
    self.name = name
    self.surname = surname
    self.dad_name = dad_name

  def __str__(self):
    return f"{self.name}_{self.surname} : {self.dad_name}'s ze"

p1 = Person("Zura", "Beqauri", "temuri")

print(p1)


