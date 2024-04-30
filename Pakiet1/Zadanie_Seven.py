words = ["apple", "banana", "orange", "kiwi", "strawberry", "grape"]

filtered_words = list(filter(lambda x: len(x) > 5, words))
print(filtered_words)  

# Wynik: ['banana', 'orange', 'strawberry']
