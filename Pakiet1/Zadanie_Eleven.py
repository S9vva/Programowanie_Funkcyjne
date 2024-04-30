def sortuj_po_dlugosci(lista_stringow):
    return sorted(lista_stringow, key=lambda x: len(x))

lista = ["jabłko", "gruszka", "banan", "ananas", "mango"]
posortowana_lista = sortuj_po_dlugosci(lista)
print(posortowana_lista)
