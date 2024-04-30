def remove_duplicates(input_list):
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

original_list = [1, 2, 3, 2, 4, 5, 3, 6, 7, 8, 7, 9]
unique_list = remove_duplicates(original_list)
print("Original list:", original_list)
print("Lista bez zduplikowanych elementóww:", unique_list)

#Wynik: Original list: [1, 2, 3, 2, 4, 5, 3, 6, 7, 8, 7, 9]
#Lista bez zduplikowanych elementóww: [1, 2, 3, 4, 5, 6, 7, 8, 9]
