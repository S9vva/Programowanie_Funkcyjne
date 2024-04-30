def check_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)


word1 = "listen"
word2 = "silent"
print(check_anagrams(word1, word2))

#Wynik : True
