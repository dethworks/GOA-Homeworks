                                     # 1
def filter_list(lst):
    result = []

    for item in lst:
        if type(item) == int:
            result.append(item)

    return result


                                     # 2
def disemvowel(string_):
    result = ""  
    vowels = "aeiouAEIOU"  
    for char in string_:  
        if char not in vowels:  
            result += char  
    return result  

                                    # 3

def descending_order(n):
    num_str = str(n)
    num_list = []
    
    for digit in num_str:
        num_list.append(digit)
    
    num_list.sort(reverse=True)
    
    sorted_str = ""
    for digit in num_list:
        sorted_str += digit
    
    sorted_number = int(sorted_str)
    return sorted_number


