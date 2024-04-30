from collections import Counter

def najczesciej_wystepujacy_element(lista):
    licznik = Counter(lista)
    najczestszy_element = licznik.most_common(1)[0][0]
    return najczestszy_element

moja_lista = [1, 2, 3, 2, 2, 4, 5, 2, 6, 7, 2]
wynik = najczesciej_wystepujacy_element(moja_lista)
print("Najczęściej występujący element:", wynik)

#Wynik - Najczęściej występujący element: 2