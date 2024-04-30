from collections import defaultdict

def polacz_slowniki(*slowniki):
    wynikowy_slownik = defaultdict(int)
    for slownik in slowniki:
        for klucz, wartosc in slownik.items():
            wynikowy_slownik[klucz] += wartosc
    return dict(wynikowy_slownik)

slownik1 = {'a': 1, 'b': 2, 'c': 3}
slownik2 = {'b': 3, 'c': 4, 'd': 5}
slownik3 = {'c': 1, 'd': 2, 'e': 3}
wynik = polacz_slowniki(slownik1, slownik2, slownik3)
print("Połączony słownik:", wynik)

# Wynik - Połączony słownik: {'a': 1, 'b': 5, 'c': 8, 'd': 7, 'e': 3}
