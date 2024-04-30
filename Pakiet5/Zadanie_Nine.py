from functools import reduce

numbers = [4, 7, 2, 9, 3, 6]
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print("Największa liczba:", max_number)

# Największa liczba: 9

from functools import reduce

numbers = [4, 7, 2, 9, 3, 6]
average = reduce(lambda x, y: x + y, numbers) / len(numbers)
print("Średnia:", average)

#Średnia: 5.166666666666667
