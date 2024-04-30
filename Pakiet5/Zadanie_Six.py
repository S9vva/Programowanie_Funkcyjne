words = ["apple", "banana", "orange", "apricot", "grape"]

words_starting_with_a = list(filter(lambda word: word.startswith('a'), words))
print("Słowa zaczynające się na 'a':", words_starting_with_a)

numbers = [1, 2, 3, 4, 5]

# Przekształcenie listy liczb w listę ich kwadratów przy użyciu map()
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Kwadraty liczb:", squared_numbers)

#Słowa zaczynające się na 'a': ['apple', 'apricot']
#Kwadraty liczb: [1, 4, 9, 16, 25]