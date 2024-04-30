def suma_krotek(krotka1, krotka2):
    if len(krotka1) != len(krotka2):
        raise ValueError("Krotki muszą mieć tę samą długość")

    suma = tuple(x + y for x, y in zip(krotka1, krotka2))
    return suma

krotka1 = (1, 2, 3)
krotka2 = (4, 5, 6)
wynik = suma_krotek(krotka1, krotka2)
print(wynik)


#Wynik: (5,7,9)
