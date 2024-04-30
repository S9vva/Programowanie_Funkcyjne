
def potegi_liczby_2():
    liczba = 1
    while True:
        yield liczba
        liczba *= 2

generator = potegi_liczby_2()


for _ in range(5):
    print(next(generator))  # Wartość jest obliczana leniwie
