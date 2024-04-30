
def custom_sort(lst, key_func):
    return sorted(lst, key=key_func)


my_list = ['banana', 'apple', 'cherry', 'date']
sorted_list = custom_sort(my_list, key_func=len)
print("Posortowana lista -", sorted_list)

#Wynik : Posortowana lista - ['date', 'apple', 'banana', 'cherry']