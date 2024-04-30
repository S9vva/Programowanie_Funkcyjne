from itertools import groupby

class Zadanie_Seven:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def group_by_parity(self):
        def is_even(n):
            return n % 2 == 0
        
        sorted_numbers = sorted(self.numbers, key=is_even)
        
        grouped = groupby(sorted_numbers, key=is_even)
        
        for is_even, group in grouped:
            parity = "Parzyste" if is_even else "Nieparzyste"
            print(f"{parity} liczby:", list(group))

#Nieparzyste liczby: [1, 3, 5, 7, 9]
#Parzyste liczby: [2, 4, 6, 8, 10]