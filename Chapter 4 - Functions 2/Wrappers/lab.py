import time
import functools


def count_time_wrapper(func):
    def count_time(*args, **kwargs):
        start = time.time()
        print(f"Starting function {func.__name__}")
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time spent on {func.__name__}: {end-start}")
        return result
    return count_time


@count_time_wrapper
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v


print(get_sequence(18))