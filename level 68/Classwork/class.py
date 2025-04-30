#                                                          1

#  შემქნეით lambda-ს ფუნქცია, lambda-ს უნდა ჰქონდეს  3 არგუმენტი და უნდა გამოთვალო მისი საშვალო

average = lambda num1, num2, num3 : (num1 + num2 + num3) / 3

print(average(2, 3 ,4))

#                                                          2

even_or_odd = lambda number : "Even" if number % 2 == 0 else "Odd"

print(even_or_odd(5))

#                                                          3

positive_sum = lambda arr : sum( x for x in  arr if x > 0 )

print(positive_sum([1, 2, 5, -2, -3]))

#                                                          4

find_smallest_int  = lambda arr : min(arr)

print(find_smallest_int([1, 3, 5, 42]))

#                                                          5

count_by = lambda x, n: [x * i for i in range(1, n + 1)]

print(count_by(3, 4))