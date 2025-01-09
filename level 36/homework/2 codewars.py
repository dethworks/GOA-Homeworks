def square_digits(n):
    n_str = str(n)
    result = ""
    for digit in n_str:
        result += str(int(digit) ** 2)
    return int(result)
