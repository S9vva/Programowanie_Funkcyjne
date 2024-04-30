def map_nested(func, nested_list):
    mapped_list = []
    for item in nested_list:
        if isinstance(item, list):
            mapped_list.append(map_nested(func, item))
        else:
            mapped_list.append(func(item))
    return mapped_list

def double(x):
    return x * 2

nested_list = [1, [2, 3], [4, 5, [6, 7]], 8]
mapped_result = map_nested(double, nested_list)
print("Oryginalna zagnieżdzona lista", nested_list)
print("Zmapowana zagnieżdzona lista:", mapped_result)

#Wynik : Oryginalna zagnieżdzona lista [1, [2, 3], [4, 5, [6, 7]], 8]
# Zmapowana zagnieżdzona lista: [2, [4, 6], [8, 10, [12, 14]], 16]
