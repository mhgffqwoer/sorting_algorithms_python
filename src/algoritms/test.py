from time import *


def test(func, array):
    start_time = time_ns()
    array = func(array)
    finish_time = time_ns() - start_time
    return int(finish_time/1_000)