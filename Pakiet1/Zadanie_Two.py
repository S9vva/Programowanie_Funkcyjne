def make_multiplier(multiplier):
    def multiplier_function(x):
        return x * multiplier
    return multiplier_function


multiply_by_3 = make_multiplier(3)
print(multiply_by_3(5))  # Wynik: 15 (bo 5 * 3 = 15)

multiply_by_10 = make_multiplier(10)
print(multiply_by_10(7))  # Wynik: 70 (bo 7 * 10 = 70)
