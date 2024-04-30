from functools import partial
import operator

mnozenie_przez_3_partial = partial(operator.mul, 3)

# Testowanie
print(mnozenie_przez_3_partial(5))  # Powinno zwrócić 15
print(mnozenie_przez_3_partial(10))  # Powinno zwrócić 30
