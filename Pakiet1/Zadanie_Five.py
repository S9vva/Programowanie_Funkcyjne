numbers = [1, 2, 3, 4, 5]

square_function = lambda x: x ** 2

squared_numbers = list(map(square_function, numbers))
print(squared_numbers)  

# Wynik: [1, 4, 9, 16, 25]
