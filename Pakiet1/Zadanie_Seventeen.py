from functools import partial

def dodaj(x, y):
    return x + y

dodaj_5 = partial(dodaj, 5)

# Testowanie
print(dodaj_5(10))  # Powinno zwrócić 15 (10 + 5)
print(dodaj_5(3))   # Powinno zwrócić 8 (3 + 5)
