def compose(f, g):
    def composed_function(x):
        return f(g(x))
    return composed_function


def double(x):
    return 2 * x

def square(x):
    return x ** 2

composed = compose(double, square)


result = composed(3)  # Pierw kwadrat 3, potem podwój
print(result)  # Powinno zwrócić 18 ((3^2) * 2)
