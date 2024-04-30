def add(x):
    def add_inner(y):
        return x + y
    return add_inner

# Testowanie funkcji
add_5 = add(5)  # Uzyskujemy funkcję, która dodaje 5 do swojego argumentu
print(add_5(3)) # Powinno zwrócić 8 (5 + 3)

add_10 = add(10) # Uzyskujemy funkcję, która dodaje 10 do swojego argumentu
print(add_10(7)) # Powinno zwrócić 17 (10 + 7)
