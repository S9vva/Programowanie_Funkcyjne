def zzip_with_index(lista):
    zzipped_list = [(element, index) for index, element in enumerate(lista)]
    return zzipped_list

original_list = ["a", "b", "c", "d", "e"]
zzipped_result = zzip_with_index(original_list)
print("Oryginalna lista:", original_list)
print("Zzipowana lista z indeksami:", zzipped_result)

#Wynik : ryginalna lista: ['a', 'b', 'c', 'd', 'e']
# Zzipowana lista z indeksami: [('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4)]
