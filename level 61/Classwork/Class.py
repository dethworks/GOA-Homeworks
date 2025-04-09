# 1
def greet():
    return "hello world!"

# 2
def make_upper_case(s):
    return s.upper()

# 3
def repeat_str(repeat, string):
    return string * repeat

# 4
def no_space(x):
    return x.replace(' ', '')

# 5
def create_array(n):
    res = []
    i = 1
    while i <= n: 
        res += [i]
        i += 1
    return res

# 6
def maps(a):
    return [i * 2 for i in a]

# 7
def grader(s):
    if s > 1 or s < 0.6: return 'F'
    if s >= 0.9: return 'A'
    if s >= 0.8: return 'B'
    if s >= 0.7: return 'C'
    if s >= 0.6: return 'D'

# 8
websites = ['codewars'] * 1000

# 9
def double_char(s):
    return ''.join(i * 2 for i in s)

# 10
def people_with_age_drink(age):
    if age < 14: return "drink toddy"
    if age < 18: return 'drink coke'
    if age < 21: return 'drink beer'
    if age >= 21: return 'drink whisky'

# 11
def bonus_time(salary, bonus):
    return "$" + str(salary * 10) if bonus else "$" + str(salary)

# 12
def monkey_count(n):
    return [i for i in range(1, n + 1)]
