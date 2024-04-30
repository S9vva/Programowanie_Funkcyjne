def filtruj_parzyste_wartosci(slownik):
    nowy_slownik = {}
    for klucz, wartosc in slownik.items():
        if isinstance(wartosc, int) and wartosc % 2 == 0:
            nowy_slownik[klucz] = wartosc
    return nowy_slownik

# Przykładowe użycie funkcji:
slownik = {'a': 3, 'b': 6, 'c': 9, 'd': 12, 'e': 15}
wynik = filtruj_parzyste_wartosci(slownik)
print("Nowy słownik zawierający tylko parzyste wartości:", wynik)

#Nowy słownik zawierający tylko parzyste wartości: {'b': 6, 'd': 12}