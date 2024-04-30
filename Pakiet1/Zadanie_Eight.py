from functools import reduce
import operator

numbers = [1, 2, 3, 4, 5]

sum_of_numbers = reduce(operator.add, numbers)
print(sum_of_numbers)  

# Wynik: 15
