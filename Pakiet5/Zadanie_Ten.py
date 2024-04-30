def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def read_large_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.rstrip()


# Przykładowe użycie dla generatora sekwencji Fibonacciego
fib = fibonacci_sequence()
for _ in range(10):
    print(next(fib))
