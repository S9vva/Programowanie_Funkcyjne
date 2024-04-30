def generate_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci_generator = generate_fibonacci()
for _ in range(10):  
    print(next(fibonacci_generator))

#Wynik: 0 1 1 2 3 5 8 13 21 34
