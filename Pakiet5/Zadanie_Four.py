def apply_function(func, x):
     return func(x)

def square(num):
      return num ** 2

def cube(num):
      return num ** 3


result1 = apply_function(square, 4)
print("Kwadrat liczby 4:", result1)

#Kwadrat liczby 4: 16

result2 = apply_function(cube, 3)
print("Sześcian liczby 3:", result2) 

#Sześcian liczby 3: 27