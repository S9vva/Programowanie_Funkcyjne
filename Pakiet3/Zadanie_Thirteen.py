def split_list(lst, chunk_size):
    if chunk_size <= 0:
        return None  
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 3
print(split_list(my_list, chunk_size))  

# Wynik: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
