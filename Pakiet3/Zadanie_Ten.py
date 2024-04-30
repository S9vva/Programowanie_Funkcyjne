def cumulative_sum(lista):
    cumulative_sum_list = []
    running_sum = 0
    for element in lista:
        running_sum += element
        cumulative_sum_list.append(running_sum)
    return cumulative_sum_list

# Przykładowe użycie funkcji:
original_list = [1, 2, 3, 4, 5]
cumulative_sum_result = cumulative_sum(original_list)
print("Oryginalna lista:", original_list)
print("Suma skumulowana lista:", cumulative_sum_result)

#Wynik : Oryginalna lista: [1, 2, 3, 4, 5]
# Suma skumulowana lista: [1, 3, 6, 10, 15]
