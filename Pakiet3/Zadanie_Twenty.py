
def sum_of_squares_of_odds(numbers):
    return sum(x**2 for x in numbers if x % 2 != 0)


my_numbers = [1, 2, 3, 4, 5, 6, 7 ,8]
sum_squares = sum_of_squares_of_odds(my_numbers)
print("Suma nieparzystych kwadratów -", sum_squares)

#Wynik : Suma nieparzystych kwadratów - 84