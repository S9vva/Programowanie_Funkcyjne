get_even_numbers = lambda numbers: [num for num in numbers if num % 2 == 0]

calculate_rectangle_area = lambda length, width: length * width

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)
print("Liczby parzyste:", even_numbers)

length = 5
width = 4
area = calculate_rectangle_area(length, width)
print("Pole prostokąta:", area)

#Liczby parzyste: [2, 4, 6, 8, 10]
#Pole prostokąta: 20