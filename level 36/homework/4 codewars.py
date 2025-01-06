def square_digits(num):
    num_str = str(num) 
    squared_digits = []  
    
    for digit in num_str:
        squared_digit = int(digit) ** 2 
        squared_digits.append(str(squared_digit))
        
    result = ''.join(squared_digits)  
    return int(result)  