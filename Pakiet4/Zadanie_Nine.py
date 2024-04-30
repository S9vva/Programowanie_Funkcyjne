def map_tuples(lst, func):
    return [func(tpl) for tpl in lst]

print(map_tuples([(1, 2), (3, 4)], lambda tpl: tpl[0] * tpl[1]))

# Wynik - [2, 12]