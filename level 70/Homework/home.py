                                                    # 1

double_char = lambda s: ''.join([c * 2 for c in s])
                                                    # 2

get_average = lambda marks: sum(marks) // len(marks)
                                                    # 3
def get_planet_name(id):
    name = ""
    if id == 1:
        name = "Mercury"
    elif id == 2:
        name = "Venus"
    elif id == 3:
        name = "Earth"
    elif id == 4:
        name = "Mars"
    elif id == 5:
        name = "Jupiter"
    elif id == 6:
        name = "Saturn"
    elif id == 7:
        name = "Uranus"
    elif id == 8:
        name = "Neptune"
    return name
                                                   # 4

sum_str = lambda a, b: str((int(a) if a else 0) + (int(b) if b else 0))
                                                  # 5

def merge_arrays(arr1, arr2):
    return sorted(set(arr1 + arr2))
