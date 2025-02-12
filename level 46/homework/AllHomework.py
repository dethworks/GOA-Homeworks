# task 1
def high_and_low(n):
    nums = n.split()
    max_num = max(nums, key=int)
    min_num = min(nums, key=int)
    return max_num + ' ' + min_num

high_and_low("1 9 3 4 -5")

# task 2
def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        return pin.isdigit()
    return False

validate_pin('4353')

# task 3
def odd_or_even(arr):
    total = sum(arr)
    if total % 2 == 0:
        return 'even'
    return 'odd'

odd_or_even([1023, 1, 2])

# task 4
def solution(nums):
    if len(nums) == 0:
        return []
    nums.sort()
    return nums

solution([20, 2, 10])

# task 5
def greet(name):
    return 'Hello ' + name.capitalize() + '!'

greet('BILLY')
