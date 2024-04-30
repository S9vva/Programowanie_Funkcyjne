def list_map(lst, func):
    return [func(x) for x in lst]


print(list_map([1, 2, 3, 4], lambda x: x * 2))

# Wynik - [2, 4, 6, 8]