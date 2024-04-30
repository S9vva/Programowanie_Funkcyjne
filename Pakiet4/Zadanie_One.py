def suma_parzystych(lista):
    suma = 0
    for liczba in lista:
        if liczba % 2 == 0:  # Sprawdzenie czy liczba jest parzysta
            suma += liczba
    return suma

# Przykładowe użycie funkcji:
liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
wynik = suma_parzystych(liczby)
print("Suma parzystych liczb w liście:", wynik)

#Suma parzystych liczb w liście: 30