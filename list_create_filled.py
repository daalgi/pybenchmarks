import numpy as np
from numba import jit, prange

from base import Test


NUMBER = 8.8


def python_loop(length):
    s = []
    for i in range(length):
        s.append(NUMBER)
    return s

def python_list_mult(length):
    return [NUMBER] * length

def python_list_comprehension(length):
    return [NUMBER for _ in range(length)]

def numpy_empty_fill(length):
    return np.empty(length).fill(NUMBER)

@jit(nopython=True)
def numba_in_range(length):
    s = np.empty(length)
    for i in range(length):
        s[i] = NUMBER
    return s

@jit(nopython=True, parallel=True)
def numba_parallel(length):
    s = np.empty(length)
    for i in prange(length):
        s[i] = NUMBER
    return s

lengths = [int(1e1), int(1e2), int(1e3), int(1e4), int(1e5), int(1e6)]
repetitions = int(1e4)
for length in lengths:
    print(f"\nVECTOR LENGTH = {length:.0E} -- REPETITIONS = {repetitions}")

    if length < 2e4:
        Test(python_loop, length, repetitions=repetitions, verbose=False)
        Test(python_list_comprehension, length, repetitions=repetitions, verbose=False)
    Test(python_list_mult, length, repetitions=repetitions, verbose=False)
    Test(numpy_empty_fill, length, repetitions=repetitions, verbose=False)
    Test(numba_in_range, length, repetitions=repetitions, verbose=False)
    Test(numba_parallel, length, repetitions=repetitions, verbose=False)