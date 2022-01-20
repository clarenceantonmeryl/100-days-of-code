import time


def decorator_speed_calc(function):
    def wrapper_function():
        time_a = time.time()
        function()
        time_b = time.time()
        print(f"{function.__name__} took {time_b - time_a} seconds")
    return wrapper_function


@decorator_speed_calc
def fast_function():
    for i in range(100):
        j = i ** 2


@decorator_speed_calc
def slow_function():
    for i in range(10000):
        j = i ** 2


fast_function()
slow_function()
