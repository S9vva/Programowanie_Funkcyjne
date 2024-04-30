def rotate_list(lst, k):
    if not lst:
        return []  
    else:
        k = k % len(lst)  
        return lst[-k:] + lst[:-k]

my_list = [1, 2, 3, 4, 5]
k = 2
print(rotate_list(my_list, k))

# Output: [4, 5, 1, 2, 3]
