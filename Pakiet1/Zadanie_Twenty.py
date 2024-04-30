def analiza_struktury_danych(dane):
    if isinstance(dane, list):
        return f"To lista o długości {len(dane)}"
    elif isinstance(dane, tuple):
        return f"To krotka o długości {len(dane)}"
    elif isinstance(dane, dict):
        return f"To słownik o {len(dane)} kluczach"
    else:
        return "Nieznana struktura danych"


print(analiza_struktury_danych([1, 2, 3]))  # To lista o długości 3
print(analiza_struktury_danych((1, 2, 3, 4)))  # To krotka o długości 4
print(analiza_struktury_danych({"a": 1, "b": 2}))  # To słownik o 2 kluczach
print(analiza_struktury_danych("hello"))  # Nieznana struktura danych
