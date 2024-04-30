def remove_whitespace(lst):
    return [string.replace(" ", "") for string in lst]


my_list = ["apple ", " banana", "orange ", " kiwi "]
cleaned_list = remove_whitespace(my_list)
print(cleaned_list) 

# Wynik: ['apple', 'banana', 'orange', 'kiwi']
