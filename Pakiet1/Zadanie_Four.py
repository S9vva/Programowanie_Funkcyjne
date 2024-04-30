import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__} - {execution_time} sekund")
        return result
    return wrapper

@timeit
def example_function():
    time.sleep(2)  

example_function()

#Wynik : Czas wykonania funkcji example_function - 2.0002548694610596 sekund


