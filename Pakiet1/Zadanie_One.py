def apply_twice(func, value):
    return func(func(value))

# Przykładowe użycie funkcji:
def square(x):
    return x * x

result = apply_twice(square, 3)
print(result)  # Output: 81 (bo 3^2 = 9, a potem 9^2 = 81)
