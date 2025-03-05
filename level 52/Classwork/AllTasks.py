                                   # 1
def find_next_square(sq):
    root = sq ** 0.5

    if root == int(root):
        root2= int(root) + 1
        return root2* root2
    else:
        return -1
                                    # 2

def min_max(lst):
    if not lst: 
        return -1
    return [min(lst), max(lst)]

                                    # 3


def series_sum(n):
    total = 0  
    count = 0  
    divider = 1  

    while count < n:  
        total = total + (1 / divider)  
        divider += 3  
        count += 1  

    return "{:.2f}".format(total)  



               