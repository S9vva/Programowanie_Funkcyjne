def square(x): return x ** 2


def add_five(x): return x + 5


def apply_functions(funcs, values):
    return [[f(v) for f in funcs] for v in values]


funcs = [square, add_five]
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(apply_functions(funcs, values))  

#[[1, 6], [4, 7], [9, 8], [16, 9], [25, 10], [36, 11], [49, 12], [64, 13], [81, 14], [100, 15]]