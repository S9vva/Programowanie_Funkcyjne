def zamiana_wielkosci_liter(tekst):
    wynik = ""
    for znak in tekst:
        if znak.islower():  
            wynik += znak.upper() 
        elif znak.isupper():  
            wynik += znak.lower() 
        else:
            wynik += znak  
    return wynik

# Przykładowe użycie funkcji:
tekst = "Przykładowy TEKST Do Zamiany"
wynik = zamiana_wielkosci_liter(tekst)
print("Tekst po zamianie wielkości liter:", wynik)

# Tekst po zamianie wielkości liter: pRZYKŁADOWY tekst dO zAMIANY