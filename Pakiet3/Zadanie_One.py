def double_list_elements(input_list):
    doubled_list = [2 * x for x in input_list]
    return doubled_list

original_list = [1, 2, 3, 4, 5]
doubled_list = double_list_elements(original_list)
print("Original list:", original_list)
print("Doubled list:", doubled_list)

#Wynik: Original list: [1, 2, 3, 4, 5]
# Doubled list: [2, 4, 6, 8, 10]