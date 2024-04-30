def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    # Wywołanie rekurencyjne: n! = n * (n-1)!
    else:
        return n * calculate_factorial(n - 1)

print(calculate_factorial(5))  # Powinno zwrócić 120 (5!)
print(calculate_factorial(0))  # Powinno zwrócić 1 (0!)
print(calculate_factorial(1))  # Powinno zwrócić 1 (1!)
