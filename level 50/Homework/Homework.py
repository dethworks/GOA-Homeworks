# 1
def binary_array_to_number(arr):
    result = 0
    for digit in arr:
        result = result * 2 + digit
    return result
print(binary_array_to_number([1,1,0,1]))

                                            # 2
def lovefunc(flower1, flower2):
    if (flower1 % 2 == 0 and flower2 % 2 == 1) or (flower1 % 2 == 1 and flower2 % 2 == 0):
        return True
    else:
        return False
print(lovefunc(1,4))

                                            # 3
def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
print(is_triangle(3, 4, 5))

                                            # 4
def longest(a1, a2):
    combined_string = a1 + a2
    unique_letters = []
    
    for letter in combined_string:
        if letter not in unique_letters:
            unique_letters.append(letter)
    
    unique_letters.sort()
    result = ""
    for letter in unique_letters:
        result = result + letter
        
    return result
print(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq"))

                                            # 5
def invert(lst):
    result = []
    for number in lst:
        result.append(-number)
    return result
print(invert([1,2,3,4,5]))

                                            # 6
def open_or_senior(data):
    result = []
    for person in data:
        age = person[0]
        handicap = person[1]
        
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    
    return result
print(open_or_senior([(18, 20),(55,8),(60, 12),(70, 10)]))

                                            # 7
def grow(arr):
    result = 1
    for number in arr:
        result = result * number
    return result
print(grow([1, 2, 3, 4]))

                                            # 8
def printer_error(s):
    error_count = 0
    total_characters = len(s)
    
    for character in s:
        if character not in "abcdefghijklm":
            error_count = error_count + 1
    
    return str(error_count) + "/" + str(total_characters)

print(printer_error('abcdefghijklmnopqrstuvwxyz'))

                                            # 9
def dna_to_rna(dna):
    result = ""
    for letter in dna:
        if letter == "T":
            result = result + "U"
        else:
            result = result + letter
    return result
print(dna_to_rna("TTTTGCAT"))

                                               # 10         
def bmi(weight, height):
    bmi_value = weight / (height * height)
    
    if bmi_value <= 18.5:
        return "Underweight"
    elif bmi_value <= 25.0:
        return "Normal"
    elif bmi_value <= 30.0:
        return "Overweight"
    else:
        return "Obese"
    
print(bmi(80, 1.75))