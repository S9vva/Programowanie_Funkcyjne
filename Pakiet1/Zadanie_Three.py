def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = filter_even_numbers(numbers)
print(even_numbers)  

# Wynik: [2, 4, 6, 8]