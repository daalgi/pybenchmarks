from random import random
import numpy as np
from numba import jit, prange

from base import Test


def python_loop(length):
    s = []
    for i in range(length):
        s.append(random())
    return s

def python_list_comprehension(length):
    return [random() for _ in range(length)]

def numpy_random(length):
    return np.random.random(length)

@jit(nopython=True)
def numba_in_range(length):
    s = np.empty(length)
    for i in range(length):
        s[i] = np.random.random()
    return s

@jit(nopython=True, parallel=True)
def numba_parallel(length):
    s = np.empty(length)
    for i in prange(length):
        s[i] = np.random.random()
    return s

lengths = [int(1e1), int(1e2), int(1e3), int(1e4), int(1e5)]
repetitions = int(1e4)
for length in lengths:
    print(f"\nVECTOR LENGTH = {length:.0E} -- REPETITIONS = {repetitions}")
    
    if length < 2e4:
        Test(python_loop, length, repetitions=repetitions, verbose=False)
        Test(python_list_comprehension, length, repetitions=repetitions, verbose=False)
    Test(numpy_random, length, repetitions=repetitions, verbose=False)
    Test(numba_in_range, length, repetitions=repetitions, verbose=False)
    Test(numba_parallel, length, repetitions=repetitions, verbose=False)