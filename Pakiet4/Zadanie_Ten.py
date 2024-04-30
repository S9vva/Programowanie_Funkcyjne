from itertools import permutations

def generuj_permutacje(lista):
    return list(permutations(lista))

moja_lista = [1, 2, 3]
wynik = generuj_permutacje(moja_lista)
print("Permutacje elementów listy:", wynik)

#Wynik - Permutacje elementów listy: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
