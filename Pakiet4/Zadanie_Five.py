def podziel_liste(lista, max_dl):
    podzielone_listy = []
    for i in range(0, len(lista), max_dl):
        podzielone_listy.append(lista[i:i+max_dl])
    return podzielone_listy

moja_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maks_dl = 3
wynik = podziel_liste(moja_lista, maks_dl)
print("Podzielona lista:", wynik)

# Wynik - Podzielona lista: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
