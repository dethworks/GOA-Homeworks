                                # 1
def validate_pin(pin):
    
    return len(pin) in (4, 6) and pin.isdigit()

                                 # 2

def row_sum_odd_numbers(n):
    return n ** 3

                                 # 3

def binary_array_to_number(arr):
    binary_str = ''.join(str(digit) for digit in arr)  
    decimal_number = int(binary_str, 2)  
    return decimal_number 
                                 # 4

def min_max(lst):
    return [min(lst), max(lst)]  

                                  # 5

def divisors(n):
    divisors_list = []
  
    for i in range(2, n):
        if n % i == 0:  
            divisors_list.append(i)
    
    if not divisors_list:
        return n
    
    return divisors_list

                 

