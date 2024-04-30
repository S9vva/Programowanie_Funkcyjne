even_numbers_generator = (num for num in range(2, 1000000, 2))

for i in range(10):
    print(next(even_numbers_generator))


# 2 4 6 8 10 12 14 16 18 20