                                     # 1 




                                     # 2

def sequence_sum(begin, end, step):
    
    if begin > end:
        return 0
    
    
    total = 0

    current = begin
    while current <= end:              
        total += current
        current += step
    
    return total
                                    # 3

def series_sum(n):
    if n == 0:
        return "0.00"
    
    total = sum(1 / (3 * i + 1) for i in range(n))
    return f"{total:.2f}"

                                     # 4


                                     # 5

def two_oldest_ages(ages):
    sorted_ages = sorted(ages)
    return [sorted_ages[-2], sorted_ages[-1]]