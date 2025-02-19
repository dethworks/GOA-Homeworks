                                   # 1

def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9

                                   # 2


def invert(lst):
    new_list = [] 
    for num in lst:  
        new_list.append(-num)  
    return new_list  



                                   # 3
def fake_bin(s):
    result = ""
    for digit in s: 
        if int(digit) < 5: 
            result += "0"   
        else: 
            result += "1"   
    return result
                                   # 4
def string_to_array(s):
    return s.split() if s else [""]  

                                   # 5

def rps(player1, player2):
    if player1 == player2:
        return "Draw!"
    
    options = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    
    if options[player1] == player2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"




                                   # 6


def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"




                                   # 7

def monkey_count(n):
    numbers = [] 
    for i in range(1, n + 1):  
        numbers.append(i)  
    return numbers

                                   # 8

def human_years_cat_years_dog_years(humanYears):
    if humanYears == 1:
        return [1, 15, 15]
    elif humanYears == 2:
        return [2, 24, 24]
    else:
        cat_years = 24 + (humanYears - 2) * 4
        dog_years = 24 + (humanYears - 2) * 5
        return [humanYears, cat_years, dog_years]

                                   # 9

def is_isogram(string):
    seen_letters = []
    for letter in string:
        if letter.lower() in seen_letters:
            return False
        seen_letters.append(letter.lower())
    return True

                                   # 10

def binary_array_to_number(arr):
    binary_string = ""
    for num in arr:
        binary_string += str(num)
    
    return int(binary_string, 2)



