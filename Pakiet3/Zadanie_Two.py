def filter_long_words(string_list):
    # Oblicz średnią długość stringów w liście
    average_length = sum(len(word) for word in string_list) / len(string_list)
    
    # Filtruj stringi, które mają długość większą niż średnia
    filtered_list = [word for word in string_list if len(word) > average_length]
    
    return filtered_list

words_list = ["apple", "banana", "orange", "kiwi", "grapefruit", "strawberry"]
filtered_words = filter_long_words(words_list)
print("Original list:", words_list)
print("Filtered list (słowa dłuższe niż średnia długość):", filtered_words)

# Wynik: Original list: ['apple', 'banana', 'orange', 'kiwi', 'grapefruit', 'strawberry']
# Filtered list (słowa dłuższe niż średnia długość): ['grapefruit', 'strawberry']
