                       #1
def string_to_array(s):
    if s == "":
        return ['']
    return s.split()
                       #2
def string_to_number(s):
    return int(s)
                       #3
def string_to_number(s):      #(იგივეა იგივე ჩააგდო დავითმა)
    return int(s)                    

                       #4
def fake_bin(s):
    result = []
    for char in s:
        if int(char) < 5:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)
                        #5
def high_and_low(numbers):
    nums = numbers.split()  
    highest = max(int(n) for n in nums)  
    lowest = min(int(n) for n in nums)  
    return f"{highest} {lowest}"  

