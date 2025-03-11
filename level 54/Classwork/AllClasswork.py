                                    # 1

def angle(n):

    sum = (n - 2) * 180

    return sum

                                     # 2

def solution(arr):

    if arr is None or len(arr) == 0:
        return []

    return sorted(arr)


                                     # 3

def in_asc_order(arr):
    if len(arr) == 0 or len(arr) == 1:
        return True
    
    i = 0
    while i < len(arr) - 1:
        current_number = arr[i]
        next_number = arr[i + 1]
        
        if current_number > next_number:
            return False
        
        i = i + 1
    
    return True



