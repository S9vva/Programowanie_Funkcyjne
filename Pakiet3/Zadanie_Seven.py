def flatten_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list


nested_list = [1, [2, 3], [4, 5, [6, 7]], 8]
flattened_result = flatten_list(nested_list)
print("Oryginalna zagnieżdzona lista:", nested_list)
print("Spłaszczona lista:", flattened_result)

#Wynik : Oryginalna zagnieżdzona lista: [1, [2, 3], [4, 5, [6, 7]], 8]
# Spłaszczona lista: [1, 2, 3, 4, 5, 6, 7, 8]