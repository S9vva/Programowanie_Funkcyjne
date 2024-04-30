def create_exponential_function(exponent):
    return lambda x: x ** exponent

square = create_exponential_function(2)
print(square(3))  

# 9