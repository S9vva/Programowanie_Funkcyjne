def find_max_min_diff(lst):
    if not lst:
        return None  
    else:
        max_val = max(lst)
        min_val = min(lst)
        return max_val - min_val


numbers = [5, 3, 8, 1, 9, 4]
print(find_max_min_diff(numbers))

#Wynik: 8
