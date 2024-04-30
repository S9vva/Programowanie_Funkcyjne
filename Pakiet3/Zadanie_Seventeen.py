def capitalize_all_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())


text = "hello world, how are you?"
capitalized_text = capitalize_all_words(text)
print(capitalized_text)  

# Wynik: 'Hello World, How Are You?'
