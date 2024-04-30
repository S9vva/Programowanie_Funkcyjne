def add(a, b):
    result = a + b  # result jest zmienną lokalną w funkcji add
    return result

global_var = 10  # zmienna globalna

def multiply(x):
    return x * global_var  # korzystanie ze zmiennej globalnej w funkcji multiply

def generate_multiplier(n):
    def multiplier(x):
        return x * n  # korzystanie ze zmiennej n, która jest zmienną funkcji
    return multiplier

# Użycie funkcji ze zmienną funkcji
double = generate_multiplier(2)
triple = generate_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15

